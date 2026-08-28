"""
preprocessamento.py
====================
Segunda etapa do pipeline (Pre-processamento + Extracao de features,
conforme o diagrama de arquitetura do artigo).

Recebe o dataset bruto de codigos (dataset_codigos.csv, gerado por
construir_dataset.py) e produz uma matriz de atributos numericos
(features estruturais/sintaticas) pronta para o treinamento do modelo.

ETAPAS DE PRE-PROCESSAMENTO APLICADAS
--------------------------------------
1. Limpeza anti-vazamento de rotulo (label leakage):
   - remove comentarios "# DEFEITO (...)" inseridos apenas para
     documentacao/auditoria humana do dataset sintetico. Codigo real
     nao vem anotado dizendo onde esta o proprio defeito -- deixar
     esse comentario society tornaria a tarefa trivial e o modelo
     aprenderia a "ler o rotulo" em vez de aprender o padrao
     estrutural do defeito.
   - remove QUALQUER comentario (linhas iniciadas por "#"), pois em
     codigo real comentarios sao ruido para esta tarefa e nao devem
     influenciar a classificacao estrutural.
2. Normalizacao textual: remove linhas em branco extras, espacos
   finais e uniformiza quebras de linha.
3. Anonimizacao de identificadores: os NOMES das funcoes ja foram
   removidos na etapa anterior (construir_dataset.py mantém apenas o
   corpo). Aqui, adicionalmente, nomes de variaveis nao influenciam a
   extracao de features (que e estrutural/sintatica, baseada na AST,
   e nao lexica), entao nao ha vazamento via nomes de variaveis.
4. Extracao de features estruturais/sintaticas via modulo `ast` do
   Python (parsing da arvore de sintaxe abstrata), capturando:
   - contagem de lacos for/while, condicionais, retornos
   - contagem de operadores aritmeticos, relacionais e logicos
   - profundidade maxima de aninhamento de blocos
   - numero de atribuicoes e de acessos a indice (subscript)
   - numero de chamadas de funcao e de chamadas recursivas
   - heuristica de "uso antes de atribuicao" (sinal fortemente
     relacionado a defeitos de Inicializacao)
   - tamanho do codigo (linhas, tokens aproximados)
   - presenca de estruturas de controle especificas (break/continue)
   - numero de literais (constantes) numericas e de string

Uso:
    python3 preprocessamento.py
Gera:
    ../resultados/dataset_features.csv
"""

import ast
import csv
import os
import re

import pandas as pd

ENTRADA_CSV = os.path.join(os.path.dirname(__file__), "..", "resultados", "dataset_codigos.csv")
SAIDA_CSV = os.path.join(os.path.dirname(__file__), "..", "resultados", "dataset_features.csv")


# ------------------------------------------------------------------
# 1. LIMPEZA / ANTI-VAZAMENTO
# ------------------------------------------------------------------

def limpar_codigo(codigo: str) -> str:
    """Remove comentarios (incluindo o comentario '# DEFEITO (...)' que
    indicaria diretamente a categoria) e normaliza espacos em branco."""
    linhas_limpas = []
    for linha in codigo.split("\n"):
        # remove comentario de linha inteira ou apos codigo (heuristica simples:
        # nao lida com '#' dentro de strings, mas os snippets deste dataset nao
        # usam '#' como caractere de dado, entao a heuristica e segura aqui)
        if "#" in linha:
            linha = linha.split("#", 1)[0]
        linha = linha.rstrip()
        linhas_limpas.append(linha)
    texto = "\n".join(linhas_limpas)
    # remove linhas totalmente em branco extras
    texto = re.sub(r"\n\s*\n+", "\n", texto).strip("\n")
    return texto


# ------------------------------------------------------------------
# 2. EXTRACAO DE FEATURES ESTRUTURAIS/SINTATICAS (baseada em AST)
# ------------------------------------------------------------------

class ExtratorFeatures(ast.NodeVisitor):
    """Percorre a AST de um trecho de codigo (envolvido artificialmente
    em 'def _snippet(...):' para ser parseavel) e acumula contadores
    estruturais/sintaticos."""

    def __init__(self):
        self.num_for = 0
        self.num_while = 0
        self.num_if = 0
        self.num_elif_else = 0
        self.num_return = 0
        self.num_break = 0
        self.num_continue = 0
        self.num_atribuicoes = 0
        self.num_atribuicoes_aumentadas = 0  # += -= *= etc.
        self.num_subscript = 0  # acessos tipo lista[i]
        self.num_chamadas_funcao = 0
        self.num_chamadas_recursivas = 0
        self.num_op_aritmeticos = 0
        self.num_op_relacionais = 0
        self.num_op_logicos = 0
        self.num_literais_numericos = 0
        self.num_literais_string = 0
        self.num_comparacoes_none = 0
        self.profundidade_maxima = 0
        self._profundidade_atual = 0
        self.nomes_definidos_antes_uso = set()
        self.usos_antes_definicao = 0
        self._nome_funcao_atual = None

    # --- controle de profundidade de aninhamento ---
    def _visitar_bloco(self, node):
        self._profundidade_atual += 1
        self.profundidade_maxima = max(self.profundidade_maxima, self._profundidade_atual)
        self.generic_visit(node)
        self._profundidade_atual -= 1

    def visit_For(self, node):
        self.num_for += 1
        self._visitar_bloco(node)

    def visit_While(self, node):
        self.num_while += 1
        self._visitar_bloco(node)

    def visit_If(self, node):
        self.num_if += 1
        if node.orelse:
            self.num_elif_else += 1
        self._visitar_bloco(node)

    def visit_Return(self, node):
        self.num_return += 1
        self.generic_visit(node)

    def visit_Break(self, node):
        self.num_break += 1
        self.generic_visit(node)

    def visit_Continue(self, node):
        self.num_continue += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.num_atribuicoes += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.num_atribuicoes_aumentadas += 1
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.num_subscript += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        self.num_chamadas_funcao += 1
        if isinstance(node.func, ast.Name) and node.func.id == self._nome_funcao_atual:
            self.num_chamadas_recursivas += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self._nome_funcao_atual = node.name
        self.generic_visit(node)

    def visit_BinOp(self, node):
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div,
                                 ast.FloorDiv, ast.Mod, ast.Pow)):
            self.num_op_aritmeticos += 1
        self.generic_visit(node)

    def visit_Compare(self, node):
        self.num_op_relacionais += len(node.ops)
        for comparador in node.comparators:
            if isinstance(comparador, ast.Constant) and comparador.value is None:
                self.num_comparacoes_none += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.num_op_logicos += 1
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            self.num_literais_numericos += 1
        elif isinstance(node.value, str):
            self.num_literais_string += 1
        self.generic_visit(node)


def detectar_uso_antes_definicao(arvore) -> int:
    """Heuristica simples e local (nao substitui um verificador de fluxo de
    dados completo) para sinalizar possivel uso de variavel antes de
    atribuicao dentro do MESMO bloco sequencial de instrucoes -- sinal
    fortemente correlacionado com defeitos de 'Inicializacao'.
    Percorre a sequencia de instrucoes de nivel superior da funcao e
    verifica, para cada 'Name' carregado (uso), se ja apareceu do lado
    esquerdo de uma atribuicao ou como alvo de 'for'/parametro em algum
    ponto anterior do codigo (aproximacao por ordem textual)."""
    definidos = set()
    ocorrencias_uso_antes = 0

    func_node = None
    for node in ast.walk(arvore):
        if isinstance(node, ast.FunctionDef):
            func_node = node
            break
    if func_node is None:
        return 0

    definidos.update(arg.arg for arg in func_node.args.args)

    def visitar_em_ordem(node):
        nonlocal ocorrencias_uso_antes
        if isinstance(node, ast.Assign):
            # primeiro avalia o lado direito (pode usar variaveis)
            for sub in ast.walk(node.value):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                    if sub.id not in definidos:
                        ocorrencias_uso_antes += 1
            for alvo in node.targets:
                for sub in ast.walk(alvo):
                    if isinstance(sub, ast.Name):
                        definidos.add(sub.id)
            return
        if isinstance(node, ast.AugAssign):
            alvo_nome = node.target.id if isinstance(node.target, ast.Name) else None
            if alvo_nome is not None and alvo_nome not in definidos:
                ocorrencias_uso_antes += 1
            for sub in ast.walk(node.value):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                    if sub.id not in definidos:
                        ocorrencias_uso_antes += 1
            if alvo_nome is not None:
                definidos.add(alvo_nome)
            return
        if isinstance(node, ast.For):
            for sub in ast.walk(node.iter):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                    if sub.id not in definidos:
                        ocorrencias_uso_antes += 1
            for sub in ast.walk(node.target):
                if isinstance(sub, ast.Name):
                    definidos.add(sub.id)
            for stmt in node.body:
                visitar_em_ordem(stmt)
            for stmt in node.orelse:
                visitar_em_ordem(stmt)
            return
        if isinstance(node, (ast.While, ast.If)):
            for sub in ast.walk(node.test):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                    if sub.id not in definidos:
                        ocorrencias_uso_antes += 1
            for stmt in node.body:
                visitar_em_ordem(stmt)
            for stmt in node.orelse:
                visitar_em_ordem(stmt)
            return
        if isinstance(node, ast.Return):
            if node.value is not None:
                for sub in ast.walk(node.value):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                        if sub.id not in definidos:
                            ocorrencias_uso_antes += 1
            return
        if isinstance(node, ast.Expr):
            for sub in ast.walk(node.value):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
                    if sub.id not in definidos:
                        ocorrencias_uso_antes += 1
            return

    for stmt in func_node.body:
        visitar_em_ordem(stmt)

    return ocorrencias_uso_antes


def extrair_features(codigo_limpo: str) -> dict:
    """Envolve o snippet em uma funcao valida (necessario porque os
    corpos armazenados no dataset ja vem desindentados, sem a linha
    'def ...:') e extrai as features estruturais via AST."""
    codigo_com_assinatura = "def _snippet(*args, **kwargs):\n" + "\n".join(
        "    " + linha if linha.strip() else "" for linha in codigo_limpo.split("\n")
    )
    try:
        arvore = ast.parse(codigo_com_assinatura)
    except SyntaxError:
        # nao deveria ocorrer (todo o dataset foi validado), mas mantemos
        # um fallback robusto para uso em producao com codigo arbitrario
        return None

    extrator = ExtratorFeatures()
    extrator.visit(arvore)
    uso_antes_definicao = detectar_uso_antes_definicao(arvore)

    num_linhas = len([l for l in codigo_limpo.split("\n") if l.strip()])
    num_caracteres = len(codigo_limpo)

    return {
        "num_linhas": num_linhas,
        "num_caracteres": num_caracteres,
        "num_for": extrator.num_for,
        "num_while": extrator.num_while,
        "num_lacos_total": extrator.num_for + extrator.num_while,
        "num_if": extrator.num_if,
        "num_elif_else": extrator.num_elif_else,
        "num_return": extrator.num_return,
        "num_break": extrator.num_break,
        "num_continue": extrator.num_continue,
        "num_atribuicoes": extrator.num_atribuicoes,
        "num_atribuicoes_aumentadas": extrator.num_atribuicoes_aumentadas,
        "num_subscript": extrator.num_subscript,
        "num_chamadas_funcao": extrator.num_chamadas_funcao,
        "num_chamadas_recursivas": extrator.num_chamadas_recursivas,
        "num_op_aritmeticos": extrator.num_op_aritmeticos,
        "num_op_relacionais": extrator.num_op_relacionais,
        "num_op_logicos": extrator.num_op_logicos,
        "num_literais_numericos": extrator.num_literais_numericos,
        "num_literais_string": extrator.num_literais_string,
        "num_comparacoes_none": extrator.num_comparacoes_none,
        "profundidade_maxima": extrator.profundidade_maxima,
        "uso_antes_definicao": uso_antes_definicao,
        "razao_atribuicoes_por_linha": round(
            (extrator.num_atribuicoes + extrator.num_atribuicoes_aumentadas) / num_linhas, 3
        ) if num_linhas else 0,
        "razao_subscript_por_linha": round(extrator.num_subscript / num_linhas, 3) if num_linhas else 0,
    }


def main():
    df = pd.read_csv(ENTRADA_CSV)
    print(f"Exemplos carregados: {len(df)}")

    linhas_saida = []
    falhas = 0
    for _, row in df.iterrows():
        codigo_limpo = limpar_codigo(row["codigo"])
        features = extrair_features(codigo_limpo)
        if features is None:
            falhas += 1
            continue
        registro = {
            "id": row["id"],
            "algoritmo": row["algoritmo"],
            "categoria": row["categoria"],
            "codigo_limpo": codigo_limpo,
        }
        registro.update(features)
        linhas_saida.append(registro)

    if falhas:
        print(f"AVISO: {falhas} exemplos falharam na extracao de features e foram descartados.")

    df_saida = pd.DataFrame(linhas_saida)
    os.makedirs(os.path.dirname(SAIDA_CSV), exist_ok=True)
    df_saida.to_csv(SAIDA_CSV, index=False)

    print(f"\nFeatures extraidas: {len(df_saida.columns) - 4} atributos numericos")
    print(f"Total de exemplos processados: {len(df_saida)}")
    print(f"Dataset de features salvo em: {os.path.abspath(SAIDA_CSV)}")

    # verificacao de sanidade anti-vazamento
    categorias = df_saida["categoria"].unique()
    vazamentos = sum(
        1 for _, r in df_saida.iterrows() if r["categoria"] in r["codigo_limpo"].lower()
    )
    print(f"\nVerificacao anti-vazamento: {vazamentos}/{len(df_saida)} exemplos ainda "
          f"contem o nome da categoria no codigo limpo (esperado: 0).")


if __name__ == "__main__":
    main()
