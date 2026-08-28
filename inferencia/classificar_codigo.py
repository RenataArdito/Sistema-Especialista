"""
classificar_codigo.py
=======================
Quarta e ultima etapa do pipeline (espelha a metade inferior do
diagrama de arquitetura do artigo):
  Modelo Treinado -> Novo Codigo (Input) -> Pre-processamento ->
  Extracao de features -> Classificacao -> Saida: tipo de erro

Carrega o modelo Random Forest treinado (modelo_random_forest.joblib)
e classifica trechos de codigo Python NAO vistos durante o treino,
retornando a categoria de defeito prevista (dentre as 7 da Tabela 2
do artigo) e a distribuicao de probabilidade entre as classes.

Uso:
    python3 classificar_codigo.py          # roda os exemplos de demonstracao abaixo
    from classificar_codigo import classificar
    classificar(meu_codigo_como_string)
"""

import os
import sys

import joblib
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "preprocessamento"))
from preprocessamento import limpar_codigo, extrair_features  # noqa: E402

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
CAMINHO_MODELO = os.path.join(BASE_DIR, "resultados", "modelo_random_forest.joblib")

_pacote = None


def _carregar_modelo():
    global _pacote
    if _pacote is None:
        _pacote = joblib.load(CAMINHO_MODELO)
    return _pacote


def classificar(codigo: str, top_n: int = 3) -> dict:
    """Recebe um trecho de codigo Python (corpo de funcao, sem a linha
    'def ...:') e retorna a categoria de defeito prevista, junto com o
    ranking de probabilidades das top_n classes mais provaveis."""
    pacote = _carregar_modelo()
    modelo = pacote["modelo"]
    codificador = pacote["codificador_rotulos"]
    colunas_features = pacote["colunas_features"]

    # ---- Pre-processamento (igual ao aplicado no treino) ----
    codigo_limpo = limpar_codigo(codigo)
    features = extrair_features(codigo_limpo)
    if features is None:
        raise ValueError("Nao foi possivel interpretar o codigo fornecido (erro de sintaxe).")

    # ---- Extracao de features (garante mesma ordem de colunas do treino) ----
    vetor = pd.DataFrame([[features[col] for col in colunas_features]], columns=colunas_features)

    # ---- Classificacao ----
    probabilidades = modelo.predict_proba(vetor)[0]
    indice_previsto = probabilidades.argmax()
    categoria_prevista = codificador.inverse_transform([indice_previsto])[0]

    ranking = sorted(
        zip(codificador.classes_, probabilidades), key=lambda x: x[1], reverse=True
    )[:top_n]

    return {
        "categoria_prevista": categoria_prevista,
        "confianca": float(probabilidades[indice_previsto]),
        "ranking": [(cat, float(p)) for cat, p in ranking],
        "features_extraidas": features,
    }


# ------------------------------------------------------------------
# DEMONSTRACAO: exemplos de codigo NOVOS, nunca vistos pelo treino,
# escritos manualmente para testar o pipeline de ponta a ponta.
# ------------------------------------------------------------------
EXEMPLOS_DEMONSTRACAO = {
    "esperado_inicializacao": """
total = 0
for item in carrinho:
    quantidade += item['quantidade']
return quantidade
""",
    "esperado_dados": """
posicoes = []
for i in range(len(matriz) + 1):
    posicoes.append(matriz[i])
return posicoes
""",
    "esperado_controle": """
indice = 0
while indice < len(fila):
    if fila[indice] == 'urgente':
        return indice
return -1
""",
    "esperado_excesso": """
total = 0
for preco in precos:
    total += preco
    total += 0
    verificacao = total == total
return total
""",
    "esperado_comissao": """
maior = precos[0]
for preco in precos:
    if preco < maior:
        maior = preco
return maior
""",
}


def main():
    print("=" * 70)
    print("DEMONSTRACAO: classificacao de codigo novo (nao visto no treino)")
    print("=" * 70)
    for nome, codigo in EXEMPLOS_DEMONSTRACAO.items():
        resultado = classificar(codigo)
        print(f"\n--- {nome} ---")
        print("Codigo:")
        print(codigo.strip())
        print(f"\n>> Categoria prevista: {resultado['categoria_prevista']} "
              f"(confianca: {resultado['confianca']:.2%})")
        print(">> Ranking top-3:")
        for cat, p in resultado["ranking"]:
            print(f"     {cat:16s}: {p:.2%}")


if __name__ == "__main__":
    main()
