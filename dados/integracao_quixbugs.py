"""
integracao_quixbugs.py
========================
Script ILUSTRATIVO de integracao com o dataset publico QuixBugs
(Lin, Koppel et al., 2017 - "QuixBugs: A Multi-Lingual Program Repair
Benchmark Set Based on the Quixey Challenge", SPLASH Companion 2017),
disponivel em: https://github.com/jkoppel/QuixBugs

MOTIVACAO
---------
O dataset construido em erros.py / construir_dataset.py e SINTETICO:
os defeitos foram inseridos manualmente por engenharia de mutacao
(inspirada em Mutation Testing), o que garante controle total sobre o
rotulo de cada exemplo mas nao captura necessariamente a "textura"
estatistica de erros reais cometidos por programadores humanos.

O QuixBugs e um excelente complemento porque:
  - contem 40 algoritmos CLASSICOS (bitcount, bucketsort,
    depth_first_search, gcd, knapsack, mergesort, quicksort, sieve,
    etc.) -- o mesmo "estilo" dos 10 algoritmos usados em erros.py
    (buscas, ordenacoes, recursao/iteracao numerica);
  - cada programa tem exatamente 1 defeito em 1 linha, extraido de
    erros REAIS cometidos por programadores no Quixey Challenge (nao
    e sintetico), o que da validade externa ao dataset combinado;
  - e pequeno e teoricamente tratavel manualmente: um especialista
    consegue classificar as 40 linhas defeituosas nas 7 categorias da
    Tabela 2 do artigo em poucas horas (o que NAO seria viavel, por
    exemplo, com o IBM CodeNet, que tem milhoes de exemplos mas
    apenas rotulos de veredito de execucao -- Accepted / Wrong Answer
    / Runtime Error / Time Limit Exceeded -- que nao correspondem
    diretamente as 7 categorias do artigo sem uma etapa adicional de
    reclassificacao manual em larga escala).

PASSO A PASSO
-------------
1. Clonar o repositorio:
     git clone https://github.com/jkoppel/QuixBugs.git

2. Cada programa em QuixBugs/python_programs/<nome>.py contem a
   versao COM defeito; a versao corrigida esta em
   QuixBugs/correct_python_programs/<nome>.py. O arquivo
   QuixBugs/json_testcases/<nome>.json contem casos de teste.

3. Para cada um dos 40 programas, calcular o DIFF entre a versao
   defeituosa e a versao corrigida (ver funcao `diff_programas`
   abaixo) para isolar a linha exata alterada.

4. Classificar manualmente (revisao humana, apoiada pela tabela de
   mapeamento heuristico `MAPEAMENTO_SUGERIDO` abaixo) cada um dos 40
   diffs em uma das 7 categorias da Tabela 2 do artigo. Um mapeamento
   heuristico inicial e sugerido a partir da propria classificacao de
   14 "defect classes" que o QuixBugs ja fornece (ver
   `QuixBugs/README.md`), mas REVISAO HUMANA e recomendada antes do
   uso, pois a taxonomia de 14 classes do QuixBugs nao equivale 1:1 as
   7 categorias do artigo.

5. Extrair o corpo da funcao defeituosa (mesmo formato usado em
   dataset_codigos.csv: coluna "codigo") e adicionar as 40 novas
   linhas ao dataset combinado, aumentando a robustez e a validade
   externa do treinamento (420 exemplos sinteticos + 40 exemplos
   reais = 460 exemplos).

6. Repetir o pipeline (preprocessamento.py -> treinar_modelo.py) sobre
   o dataset combinado.
"""

import difflib
import os

# Mapeamento heuristico INICIAL (14 classes do QuixBugs -> 7 categorias
# do artigo). Deve ser revisado manualmente linha a linha antes do uso,
# pois a correspondencia nao e perfeita.
MAPEAMENTO_SUGERIDO = {
    "incorrect comparison operator": "computacao",
    "incorrect method call": "comissao",
    "incorrect assignment operator": "computacao",
    "incorrect variable": "comissao",
    "incorrect array slice": "dados",
    "incorrect data structure constant": "dados",
    "incorrect block deletion": "excesso",  # e o inverso: bloco que deveria existir foi removido
    "missing condition": "controle",
    "missing/added +1": "dados",
    "variable swap": "comissao",
    "incorrect field dereference": "dados",
    "invert condition": "controle",
    "single line": "computacao",  # fallback generico, exige revisao caso a caso
}


def caminho_repositorio():
    """Retorna o caminho do repositorio QuixBugs. Por padrao, procura o
    clone local em dados/QuixBugs (ao lado deste script); ajuste aqui se
    tiver clonado em outro lugar."""
    caminho_local = os.path.join(os.path.dirname(__file__), "QuixBugs")
    if os.path.isdir(caminho_local):
        return caminho_local
    return os.path.join(os.path.expanduser("~"), "QuixBugs")


def diff_programas(nome_programa: str, raiz_quixbugs: str) -> str:
    """Retorna um diff unificado entre a versao defeituosa e a versao
    corrigida de um programa do QuixBugs, para localizar a linha exata
    do defeito e apoiar a classificacao manual na categoria correta."""
    caminho_defeituoso = os.path.join(raiz_quixbugs, "python_programs", f"{nome_programa}.py")
    caminho_correto = os.path.join(raiz_quixbugs, "correct_python_programs", f"{nome_programa}.py")

    with open(caminho_defeituoso, encoding="utf-8") as f:
        linhas_defeituosas = f.readlines()
    with open(caminho_correto, encoding="utf-8") as f:
        linhas_corretas = f.readlines()

    diff = difflib.unified_diff(
        linhas_corretas, linhas_defeituosas,
        fromfile=f"{nome_programa} (correto)",
        tofile=f"{nome_programa} (com defeito)",
    )
    return "".join(diff)


def listar_programas(raiz_quixbugs: str):
    pasta = os.path.join(raiz_quixbugs, "python_programs")
    return sorted(
        nome[:-3] for nome in os.listdir(pasta)
        if nome.endswith(".py") and nome != "__init__.py"
    )


def main():
    raiz = caminho_repositorio()
    if not os.path.isdir(raiz):
        print(f"Repositorio QuixBugs nao encontrado em {raiz}.")
        print("Clone-o primeiro com:")
        print("  git clone https://github.com/jkoppel/QuixBugs.git")
        return

    programas = listar_programas(raiz)
    print(f"{len(programas)} programas encontrados no QuixBugs.")
    for nome in programas:
        print(f"\n===== {nome} =====")
        print(diff_programas(nome, raiz))
        print("--> Classifique manualmente este diff em uma das 7 categorias "
              "da Tabela 2 do artigo antes de incorporar ao dataset.")


if __name__ == "__main__":
    main()
