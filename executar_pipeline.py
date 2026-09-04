"""
executar_pipeline.py
======================
Ponto de entrada unico do projeto: executa, em sequencia, as 4 etapas do
diagrama de arquitetura do artigo (Base de Dados -> Pre-processamento ->
Treinamento/Avaliacao do modelo Random Forest -> Inferencia sobre codigo
novo), mais uma 5a etapa que consolida tudo em um relatorio HTML --
sem precisar entrar em cada pasta e rodar cada script manualmente.

Nao duplica nenhuma logica: apenas chama, na ordem certa e com o
diretorio de trabalho correto, os mesmos scripts ja documentados no
README (construir_dataset.py, preprocessamento.py, treinar_modelo.py,
classificar_codigo.py, gerar_relatorio.py). Ao final, abre no navegador
uma unica pagina com metricas, comparacao com baselines, graficos,
trabalhos relacionados, limitacoes e trabalhos futuros.

Uso:
    python executar_pipeline.py
"""

import os
import subprocess
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTADOS_DIR = os.path.join(BASE_DIR, "resultados")

ETAPAS = [
    ("1/5 - Construcao da base de dados", "dados", "construir_dataset.py"),
    ("2/5 - Pre-processamento e extracao de features (AST)", "preprocessamento", "preprocessamento.py"),
    ("3/5 - Treinamento e avaliacao do modelo Random Forest", "modelo", "treinar_modelo.py"),
    ("4/5 - Inferencia sobre codigo novo (demonstracao)", "inferencia", "classificar_codigo.py"),
    ("5/5 - Geracao do relatorio consolidado (HTML)", "relatorio", "gerar_relatorio.py"),
]


def executar_etapa(titulo: str, subpasta: str, script: str) -> None:
    pasta = os.path.join(BASE_DIR, subpasta)
    print("\n" + "=" * 70, flush=True)
    print(titulo, flush=True)
    print("=" * 70, flush=True)
    inicio = time.time()
    # stdout/stderr do subprocesso sao herdados diretamente do terminal
    # (nao capturados), entao o print() acima precisa de flush explicito
    # para nao ficar bufferizado e aparecer fora de ordem no console.
    resultado = subprocess.run([sys.executable, script], cwd=pasta)
    duracao = time.time() - inicio
    if resultado.returncode != 0:
        print(f"\nERRO: '{script}' terminou com codigo {resultado.returncode}. Pipeline interrompido.", flush=True)
        sys.exit(resultado.returncode)
    print(f"\n[OK] Etapa concluida em {duracao:.1f}s", flush=True)


def mostrar_resumo() -> None:
    caminho = os.path.join(RESULTADOS_DIR, "classification_report.txt")
    if not os.path.exists(caminho):
        return
    print("\n" + "=" * 70, flush=True)
    print("RESUMO DAS METRICAS (resultados/classification_report.txt)", flush=True)
    print("=" * 70, flush=True)
    with open(caminho, encoding="utf-8") as f:
        print(f.read(), flush=True)


def main() -> None:
    print("PIPELINE DO SISTEMA ESPECIALISTA", flush=True)
    print("Base de Dados -> Pre-processamento -> Treino/Avaliacao -> Inferencia -> Relatorio", flush=True)
    inicio_total = time.time()

    for titulo, subpasta, script in ETAPAS:
        executar_etapa(titulo, subpasta, script)

    duracao_total = time.time() - inicio_total
    print("\n" + "=" * 70, flush=True)
    print(f"PIPELINE CONCLUIDA em {duracao_total:.1f}s", flush=True)
    print("=" * 70, flush=True)

    mostrar_resumo()

    print(f"\nArtefatos gerados em: {os.path.abspath(RESULTADOS_DIR)}", flush=True)
    print("Relatorio consolidado aberto no navegador (resultados/relatorio_resultados.html).", flush=True)


if __name__ == "__main__":
    main()
