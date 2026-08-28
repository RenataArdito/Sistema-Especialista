"""
construir_dataset.py
=====================
Primeira etapa do pipeline (Base de Dados, conforme o diagrama de
arquitetura do artigo): percorre o modulo erros.py, extrai o codigo-fonte
de cada funcao defeituosa via `inspect`, e organiza tudo em uma tabela
rotulada (id, algoritmo, categoria, variante, codigo).

"""

import csv
import inspect
import os
import textwrap

import erros

CATEGORIAS_VALIDAS = [
    "inicializacao",
    "computacao",
    "desempenho",
    "controle",
    "excesso",
    "dados",
    "comissao",
]

SAIDA_CSV = os.path.join(os.path.dirname(__file__), "..", "resultados", "dataset_codigos.csv")


def normalizar_corpo(codigo_fonte: str) -> str:
    """Remove a linha 'def nome(...):' e desindenta o corpo da funcao,
    de modo que o nome da funcao (que contem o rotulo da categoria, ex.
    'calcular_media_inicializacao_v1') NAO apareca no texto do codigo
    usado para extracao de features. Isso evita vazamento trivial de
    rotulo (label leakage) logo na origem dos dados."""
    linhas = codigo_fonte.strip("\n").split("\n")
    # remove a linha da assinatura "def ...(...):"
    corpo = linhas[1:]
    corpo_texto = "\n".join(corpo)
    return textwrap.dedent(corpo_texto)


def extrair_exemplos():
    exemplos = []
    membros = inspect.getmembers(erros, inspect.isfunction)
    for nome_funcao, funcao in membros:
        if funcao.__module__ != "erros":
            continue  # ignora funcoes importadas (ex.: random.randint) por engano
        if nome_funcao.endswith("_correto"):
            continue  # versoes corretas nao entram no dataset de classificacao

        # nome esperado: <algoritmo>_<categoria>_v<numero>
        partes = nome_funcao.rsplit("_v", 1)
        if len(partes) != 2 or not partes[1].isdigit():
            continue
        prefixo, variante = partes[0], int(partes[1])

        categoria_encontrada = None
        for cat in CATEGORIAS_VALIDAS:
            sufixo = f"_{cat}"
            if prefixo.endswith(sufixo):
                categoria_encontrada = cat
                algoritmo = prefixo[: -len(sufixo)]
                break
        if categoria_encontrada is None:
            continue

        codigo_fonte = inspect.getsource(funcao)
        codigo_normalizado = normalizar_corpo(codigo_fonte)

        exemplos.append(
            {
                "id": f"{algoritmo}_{categoria_encontrada}_v{variante}",
                "algoritmo": algoritmo,
                "categoria": categoria_encontrada,
                "variante": variante,
                "codigo_bruto": codigo_fonte.strip("\n"),
                "codigo": codigo_normalizado,
            }
        )
    return exemplos


def main():
    exemplos = extrair_exemplos()
    os.makedirs(os.path.dirname(SAIDA_CSV), exist_ok=True)
    with open(SAIDA_CSV, "w", newline="", encoding="utf-8") as f:
        campos = ["id", "algoritmo", "categoria", "variante", "codigo_bruto", "codigo"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for ex in exemplos:
            writer.writerow(ex)

    print(f"Total de exemplos gerados: {len(exemplos)}")
    from collections import Counter
    contagem_categoria = Counter(e["categoria"] for e in exemplos)
    contagem_algoritmo = Counter(e["algoritmo"] for e in exemplos)
    print("\nDistribuicao por categoria:")
    for cat, qtd in sorted(contagem_categoria.items()):
        print(f"  {cat:16s}: {qtd}")
    print("\nDistribuicao por algoritmo:")
    for alg, qtd in sorted(contagem_algoritmo.items()):
        print(f"  {alg:20s}: {qtd}")
    print(f"\nDataset salvo em: {os.path.abspath(SAIDA_CSV)}")


if __name__ == "__main__":
    main()
