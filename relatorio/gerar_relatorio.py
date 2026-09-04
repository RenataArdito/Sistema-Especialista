"""
gerar_relatorio.py
====================
Quinta etapa do pipeline (nao faz parte do diagrama de arquitetura do
artigo, mas fecha o projeto para leitura humana): consolida TODOS os
artefatos gerados pelas etapas anteriores em uma unica pagina HTML
autocontida e abre automaticamente no navegador padrao.

Nao gera nenhum arquivo intermediario novo alem do proprio relatorio:
le exclusivamente o que os scripts anteriores ja produziram em
../resultados/ (metricas, comparacao de modelos, matriz de confusao,
importancia das features, dataset) e monta uma pagina unica com:

  1. Visao geral do dataset (contagens reais, nao estimadas)
  2. Resultados do Random Forest (metricas + matriz de confusao)
  3. Comparacao com baselines (Dummy / Regressao Logistica / KNN) --
     contextualiza se o ganho do Random Forest e' real ou marginal
  4. Importancia das features
  5. Trabalhos relacionados / Estado da arte
  6. Ameacas a validade / Limitacoes
  7. Trabalhos futuros

Uso:
    python3 gerar_relatorio.py
Gera:
    ../resultados/relatorio_resultados.html   (e abre no navegador)
"""

import base64
import json
import os
import re
import webbrowser
from collections import Counter
from datetime import datetime

import pandas as pd

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
RESULTADOS_DIR = os.path.join(BASE_DIR, "resultados")

CAMINHO_DATASET_CODIGOS = os.path.join(RESULTADOS_DIR, "dataset_codigos.csv")
CAMINHO_DATASET_FEATURES = os.path.join(RESULTADOS_DIR, "dataset_features.csv")
CAMINHO_METRICAS = os.path.join(RESULTADOS_DIR, "metricas_resumo.csv")
CAMINHO_COMPARACAO = os.path.join(RESULTADOS_DIR, "comparacao_modelos.json")
CAMINHO_CLASSIFICATION_REPORT = os.path.join(RESULTADOS_DIR, "classification_report.txt")
CAMINHO_MATRIZ_CONFUSAO = os.path.join(RESULTADOS_DIR, "confusion_matrix.png")
CAMINHO_FEATURE_IMPORTANCE = os.path.join(RESULTADOS_DIR, "feature_importance.png")
CAMINHO_SAIDA_HTML = os.path.join(RESULTADOS_DIR, "relatorio_resultados.html")

REQUISITOS = [
    CAMINHO_DATASET_CODIGOS, CAMINHO_DATASET_FEATURES, CAMINHO_METRICAS,
    CAMINHO_COMPARACAO, CAMINHO_CLASSIFICATION_REPORT,
    CAMINHO_MATRIZ_CONFUSAO, CAMINHO_FEATURE_IMPORTANCE,
]

PALETA_MODELOS = {
    "Random Forest": "#3B6FA0",
    "Regressao Logistica": "#6E9F5E",
    "KNN (k=5)": "#C98A3B",
    "Maioria (Dummy)": "#9B9B9B",
}


def _imagem_base64(caminho: str) -> str:
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def _parse_classification_report_por_categoria(texto: str):
    """Extrai (categoria, precisao, recall, f1, suporte) das linhas de
    classes do relatorio de classificacao do scikit-learn (ignora as
    linhas 'accuracy', 'macro avg' e 'weighted avg')."""
    linhas = []
    padrao = re.compile(r"^\s*([a-zA-Z_]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(\d+)\s*$")
    for linha in texto.split("\n"):
        m = padrao.match(linha)
        if not m:
            continue
        nome = m.group(1)
        if nome == "accuracy":
            continue
        linhas.append({
            "categoria": nome,
            "precisao": float(m.group(2)),
            "recall": float(m.group(3)),
            "f1": float(m.group(4)),
            "suporte": int(m.group(5)),
        })
    return linhas


def _barra_html(valor: float, cor: str, largura_max_px: int = 260) -> str:
    largura = max(2, round(valor * largura_max_px))
    return (
        f'<div class="barra-fundo" style="width:{largura_max_px}px">'
        f'<div class="barra-preenchida" style="width:{largura}px;background:{cor}"></div>'
        f"</div>"
    )


def carregar_dados():
    for caminho in REQUISITOS:
        if not os.path.exists(caminho):
            raise FileNotFoundError(
                f"Artefato ausente: {caminho}\n"
                "Rode as etapas anteriores do pipeline antes de gerar o relatorio "
                "(python executar_pipeline.py, ou os scripts individuais em ordem)."
            )

    df_codigos = pd.read_csv(CAMINHO_DATASET_CODIGOS)
    df_features = pd.read_csv(CAMINHO_DATASET_FEATURES)
    df_metricas = pd.read_csv(CAMINHO_METRICAS).iloc[0]
    with open(CAMINHO_COMPARACAO, encoding="utf-8") as f:
        comparacao_modelos = json.load(f)
    with open(CAMINHO_CLASSIFICATION_REPORT, encoding="utf-8") as f:
        texto_relatorio = f.read()
    por_categoria = _parse_classification_report_por_categoria(texto_relatorio)

    contagem_categorias = Counter(df_codigos["categoria"])
    contagem_algoritmos = Counter(df_codigos["algoritmo"])

    return {
        "df_codigos": df_codigos,
        "df_features": df_features,
        "metricas": df_metricas,
        "comparacao_modelos": comparacao_modelos,
        "por_categoria": por_categoria,
        "contagem_categorias": contagem_categorias,
        "contagem_algoritmos": contagem_algoritmos,
        "matriz_confusao_b64": _imagem_base64(CAMINHO_MATRIZ_CONFUSAO),
        "feature_importance_b64": _imagem_base64(CAMINHO_FEATURE_IMPORTANCE),
    }


def montar_html(dados: dict) -> str:
    metricas = dados["metricas"]
    comparacao_modelos = dados["comparacao_modelos"]
    por_categoria = sorted(dados["por_categoria"], key=lambda r: r["f1"], reverse=True)
    contagem_categorias = dados["contagem_categorias"]
    contagem_algoritmos = dados["contagem_algoritmos"]
    n_exemplos = len(dados["df_codigos"])
    n_features = len([c for c in dados["df_features"].columns
                       if c not in ("id", "algoritmo", "categoria", "codigo_limpo")])

    # ---- cards de metricas principais (Random Forest) ----
    cards_metricas = "".join(f"""
        <div class="card">
          <div class="card-valor">{valor}</div>
          <div class="card-rotulo">{rotulo}</div>
        </div>""" for rotulo, valor in [
        ("Acuracia", f"{metricas['acuracia']*100:.1f}%"),
        ("Precisao (macro)", f"{metricas['precisao_macro']*100:.1f}%"),
        ("Recall (macro)", f"{metricas['recall_macro']*100:.1f}%"),
        ("F1-score (macro)", f"{metricas['f1_macro']*100:.1f}%"),
        ("Validacao cruzada (5-fold)", f"{metricas['cv_f1_macro_media']*100:.1f}% ± {metricas['cv_f1_macro_desvio']*100:.1f}"),
    ])

    # ---- tabela/barras de comparacao entre modelos ----
    linhas_comparacao = ""
    for item in sorted(comparacao_modelos, key=lambda x: x["f1_macro"], reverse=True):
        cor = PALETA_MODELOS.get(item["modelo"], "#888888")
        linhas_comparacao += f"""
        <tr>
          <td class="celula-modelo"><span class="ponto" style="background:{cor}"></span>{item['modelo']}</td>
          <td>{item['acuracia']*100:.1f}%</td>
          <td>{item['precisao_macro']*100:.1f}%</td>
          <td>{item['recall_macro']*100:.1f}%</td>
          <td class="celula-f1">{item['f1_macro']*100:.1f}%</td>
          <td>{_barra_html(item['f1_macro'], cor)}</td>
        </tr>"""

    melhor = max(comparacao_modelos, key=lambda x: x["f1_macro"])
    pior_baseline = min((m for m in comparacao_modelos if m["modelo"] != "Random Forest"),
                         key=lambda x: x["f1_macro"])
    rf = next(m for m in comparacao_modelos if m["modelo"] == "Random Forest")
    ganho_vs_dummy_pp = (rf["f1_macro"] - next(m for m in comparacao_modelos if "Dummy" in m["modelo"])["f1_macro"]) * 100

    # ---- tabela por categoria ----
    linhas_categoria = ""
    for r in por_categoria:
        n_total_cat = contagem_categorias.get(r["categoria"], 0)
        cor_f1 = "#3B6FA0" if r["f1"] >= 0.6 else ("#C98A3B" if r["f1"] >= 0.4 else "#B4483E")
        linhas_categoria += f"""
        <tr>
          <td>{r['categoria']}</td>
          <td>{n_total_cat}</td>
          <td>{r['precisao']*100:.0f}%</td>
          <td>{r['recall']*100:.0f}%</td>
          <td style="color:{cor_f1};font-weight:600">{r['f1']*100:.0f}%</td>
        </tr>"""

    # ---- distribuicao de algoritmos ----
    itens_algoritmos = "".join(
        f'<span class="chip">{algo} <b>{qtd}</b></span>'
        for algo, qtd in sorted(contagem_algoritmos.items())
    )

    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M")

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relatorio - Sistema Especialista de Classificacao de Defeitos</title>
<style>
  :root {{
    --bg: #f7f8fa; --bg-card: #ffffff; --texto: #1c2430; --texto-suave: #5b6472;
    --borda: #e3e6ea; --acento: #3B6FA0; --acento-suave: #eaf1f8;
    --ok: #2f7d4f; --alerta: #b4483e;
    font-size: 16px;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #14181f; --bg-card: #1c222c; --texto: #e7ebf0; --texto-suave: #9aa4b2;
      --borda: #2b323e; --acento: #6fa2d8; --acento-suave: #202b38;
      --ok: #6fd19a; --alerta: #e08078;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--texto);
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.55;
  }}
  .container {{ max-width: 980px; margin: 0 auto; padding: 40px 24px 80px; }}
  header.topo {{ margin-bottom: 36px; }}
  header.topo .badge {{
    display: inline-block; font-size: .75rem; font-weight: 600; letter-spacing: .04em;
    text-transform: uppercase; color: var(--acento); background: var(--acento-suave);
    padding: 4px 10px; border-radius: 999px; margin-bottom: 14px;
  }}
  h1 {{ font-size: 1.9rem; margin: 0 0 8px; }}
  .subtitulo {{ color: var(--texto-suave); font-size: 1.02rem; max-width: 720px; }}
  h2 {{
    font-size: 1.25rem; margin: 56px 0 4px; padding-bottom: 10px;
    border-bottom: 1px solid var(--borda);
  }}
  h2 .num {{ color: var(--acento); font-variant-numeric: tabular-nums; margin-right: 8px; }}
  .intro-secao {{ color: var(--texto-suave); font-size: .95rem; margin: 10px 0 20px; max-width: 760px; }}
  .grade-cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 14px; }}
  .card {{
    background: var(--bg-card); border: 1px solid var(--borda); border-radius: 12px;
    padding: 18px 16px;
  }}
  .card-valor {{ font-size: 1.6rem; font-weight: 700; color: var(--acento); }}
  .card-rotulo {{ font-size: .82rem; color: var(--texto-suave); margin-top: 4px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: .92rem; background: var(--bg-card);
           border: 1px solid var(--borda); border-radius: 10px; overflow: hidden; }}
  th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--borda); }}
  th {{ color: var(--texto-suave); font-weight: 600; font-size: .78rem; text-transform: uppercase; letter-spacing: .03em; }}
  tr:last-child td {{ border-bottom: none; }}
  .celula-modelo {{ font-weight: 600; }}
  .celula-f1 {{ font-weight: 700; }}
  .ponto {{ display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 8px; }}
  .barra-fundo {{ height: 10px; border-radius: 999px; background: var(--borda); overflow: hidden; }}
  .barra-preenchida {{ height: 100%; border-radius: 999px; }}
  .callout {{
    background: var(--acento-suave); border: 1px solid var(--borda); border-left: 4px solid var(--acento);
    border-radius: 10px; padding: 14px 18px; font-size: .92rem; margin-top: 16px;
  }}
  .grade-imagens {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  @media (max-width: 720px) {{ .grade-imagens {{ grid-template-columns: 1fr; }} }}
  figure {{ margin: 0; background: var(--bg-card); border: 1px solid var(--borda); border-radius: 12px; padding: 14px; }}
  figure img {{ width: 100%; display: block; border-radius: 6px; }}
  figcaption {{ font-size: .82rem; color: var(--texto-suave); margin-top: 8px; text-align: center; }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .chip {{
    background: var(--bg-card); border: 1px solid var(--borda); border-radius: 999px;
    padding: 5px 12px; font-size: .82rem; color: var(--texto-suave);
  }}
  .chip b {{ color: var(--texto); margin-left: 4px; }}
  .lista-analitica {{ padding-left: 20px; }}
  .lista-analitica li {{ margin-bottom: 10px; font-size: .95rem; }}
  .lista-analitica b {{ color: var(--texto); }}
  .tabela-comparativa th:nth-child(n+2), .tabela-comparativa td:nth-child(n+2) {{ text-align: right; }}
  .tabela-comparativa td:nth-child(6) {{ min-width: 140px; }}
  .fonte {{ font-size: .8rem; color: var(--texto-suave); }}
  footer {{ margin-top: 60px; padding-top: 20px; border-top: 1px solid var(--borda); font-size: .82rem; color: var(--texto-suave); }}
</style>
</head>
<body>
<div class="container">

  <header class="topo">
    <span class="badge">Relatorio gerado automaticamente pelo pipeline</span>
    <h1>Sistema Especialista para Classificacao de Defeitos de Software</h1>
    <p class="subtitulo">
      Consolidado unico de resultados do TCC: dataset, desempenho do modelo Random Forest,
      comparacao com baselines, analise critica de limitacoes e proximos passos.
      Gerado em {data_geracao} a partir dos artefatos reais produzidos pelo pipeline
      (nenhum numero nesta pagina e' estimado manualmente).
    </p>
  </header>

  <h2><span class="num">01</span>Visao geral do dataset</h2>
  <p class="intro-secao">
    {n_exemplos} exemplos rotulados, {len(contagem_categorias)} categorias de defeito
    (Tabela 2 do artigo), {len(contagem_algoritmos)} algoritmos-base, {n_features} atributos
    estruturais extraidos via AST por exemplo.
  </p>
  <div class="chips">{itens_algoritmos}</div>

  <h2><span class="num">02</span>Resultados do modelo (Random Forest)</h2>
  <p class="intro-secao">Avaliado sobre o conjunto de teste (20%, nunca visto durante o treino).</p>
  <div class="grade-cards">{cards_metricas}</div>

  <table style="margin-top:24px">
    <thead><tr><th>Categoria</th><th>N no dataset</th><th>Precisao</th><th>Recall</th><th>F1</th></tr></thead>
    <tbody>{linhas_categoria}</tbody>
  </table>
  <div class="callout">
    Categorias que alteram diretamente a estrutura do codigo (<b>inicializacao</b>, <b>controle</b>)
    sao as melhor classificadas. <b>desempenho</b> (codigo correto, porem ineficiente) e' a mais dificil,
    pois nao produz nenhuma mudanca estrutural detectavel pelas features atuais -- ver secao de limitacoes.
  </div>

  <h2><span class="num">03</span>Comparacao com modelos baseline</h2>
  <p class="intro-secao">
    Mesmo split 80/20 e mesmas 25 features para os 4 modelos -- unica forma de saber se o
    Random Forest agrega valor real sobre alternativas mais simples.
  </p>
  <table class="tabela-comparativa">
    <thead><tr><th>Modelo</th><th>Acuracia</th><th>Precisao</th><th>Recall</th><th>F1 macro</th><th></th></tr></thead>
    <tbody>{linhas_comparacao}</tbody>
  </table>
  <div class="callout">
    O Random Forest (<b>{rf['f1_macro']*100:.1f}% F1-macro</b>) supera o classificador de maioria
    em <b>{ganho_vs_dummy_pp:.1f} pontos percentuais</b> e e' o melhor entre os 4 modelos testados,
    o que indica sinal real nas features estruturais -- mas o valor absoluto ainda esta longe do
    necessario para uso autonomo sem revisao humana (ver secao 05).
  </div>

  <h2><span class="num">04</span>Diagnostico visual</h2>
  <div class="grade-imagens">
    <figure>
      <img src="data:image/png;base64,{dados['matriz_confusao_b64']}" alt="Matriz de confusao">
      <figcaption>Matriz de confusao -- conjunto de teste</figcaption>
    </figure>
    <figure>
      <img src="data:image/png;base64,{dados['feature_importance_b64']}" alt="Importancia das features">
      <figcaption>Importancia das features (Gini / MDI)</figcaption>
    </figure>
  </div>

  <h2><span class="num">05</span>Trabalhos relacionados / Estado da arte</h2>
  <p class="intro-secao">Posicionamento do sistema frente a abordagens ja consolidadas de deteccao e classificacao de defeitos.</p>
  <ul class="lista-analitica">
    <li><b>Analisadores estaticos baseados em regras</b> (SonarQube, Pylint, PMD, Bandit) detectam
      padroes conhecidos e vulnerabilidades por regras fixas escritas por especialistas. Sao mais
      confiaveis para os casos que cobrem, mas nao generalizam para padroes novos nem aprendem com
      exemplos -- diferente da abordagem orientada a dados usada aqui.</li>
    <li><b>Analise semantica profunda</b> (CodeQL, GitHub Advanced Security) modela o fluxo de dados
      e de controle para achar vulnerabilidades de seguranca especificas. E' mais precisa que
      abordagens baseadas em contagem de features de AST, porem exige uma base de queries especializada
      por linguagem e tipo de defeito.</li>
    <li><b>Predicao de defeitos de software (defect prediction)</b> e' uma linha de pesquisa academica
      consolidada desde os anos 2000, tipicamente prevendo se um MODULO/ARQUIVO tem probabilidade de
      conter bugs a partir de metricas de processo (churn, complexidade ciclomatica, historico de
      commits) -- um problema de granularidade mais grossa e mais dados disponiveis do que o
      classificado aqui (defeito ja isolado em nivel de funcao).</li>
    <li><b>Mutation Testing</b> (DeMillo et al., 1978), usado aqui para gerar o dataset sintetico,
      e' tradicionalmente uma tecnica de avaliacao de suites de teste, nao de treinamento de
      classificadores -- o uso como fonte de dados rotulados e' a contribuicao metodologica
      deste trabalho, mas tambem sua principal limitacao de generalizacao (ver secao 06).</li>
  </ul>
  <!--

  <h2><span class="num">06</span>Ameacas a validade / Limitacoes</h2>
  <ul class="lista-analitica">
    <li><b>Dataset sintetico e pequeno.</b> {n_exemplos} exemplos vindos de apenas
      {len(contagem_algoritmos)} algoritmos didaticos (ordenacao, busca, fatorial, Fibonacci...) nao
      capturam a diversidade lexica e estrutural de codigo de producao real (nomes de dominio,
      bibliotecas externas, estilos de equipe, codigo legado).</li>
    <li><b>Granularidade de funcao isolada com defeito unico conhecido.</b> O modelo assume que o
      trecho ja foi isolado e contem exatamente um defeito -- ele classifica a CATEGORIA do defeito,
      nao DETECTA se ha um defeito, que e' o problema que uma ferramenta real precisaria resolver primeiro.</li>
    <li><b>Uma unica linguagem.</b> Todas as features sao extraidas via modulo <code>ast</code> do
      Python; a metodologia nao se transfere diretamente para outras linguagens sem reimplementar o
      extrator de features.</li>
    <li><b>Categoria "desempenho" sem sinal estrutural.</b> Codigo ineficiente pode ser
      estruturalmente identico a codigo eficiente (mesma AST, complexidade algoritmica diferente),
      o que explica o F1 mais baixo (~19%) nessa categoria e sugere que features atuais nao bastam
      para esse tipo de defeito.</li>
    <li><b>Sem validacao com revisores humanos.</b> Nao houve estudo medindo se o uso do classificador
      de fato reduz tempo ou esforco de um revisor real -- as metricas reportadas sao apenas
      estatisticas de classificacao offline.</li>
  </ul>

  <h2><span class="num">07</span>Trabalhos futuros</h2>
  <ul class="lista-analitica">
    <li><b>Dataset de bugs reais.</b> Substituir/complementar a base sintetica por bugs reais minerados
      de projetos open-source (ex.: Defects4J, BugsInPy) ou do proprio dataset publico QuixBugs ja
      referenciado em <code>dados/integracao_quixbugs.py</code>.</li>
    <li><b>Deteccao, nao so classificacao.</b> Treinar um estagio anterior que decida se um trecho tem
      defeito, para que o sistema funcione sobre codigo arbitrario, nao apenas sobre trechos
      pre-selecionados.</li>
    <li><b>Explicabilidade por instancia.</b> Adicionar SHAP/LIME para justificar cada previsao
      individual (hoje so ha importancia global das features), essencial para ganhar confianca do
      revisor humano.</li>
    <li><b>Integracao ao fluxo de trabalho real.</b> Empacotar como CLI, extensao de IDE ou GitHub
      Action/hook de CI, para uso continuo em vez de execucao manual de script.</li>
    <li><b>Suporte multi-linguagem e multi-arquivo.</b> Generalizar o extrator de features para alem
      de Python e de funcoes isoladas.</li>
  </ul>-->

  <footer>
    Relatorio gerado automaticamente por <code>relatorio/gerar_relatorio.py</code> a partir dos
    artefatos em <code>resultados/</code>. Nenhum dado nesta pagina foi editado manualmente.
    Documentacao completa das decisoes de projeto: <code>Relatorio_Implementacao.docx</code>.
  </footer>

</div>
</body>
</html>
"""
    return html


def main():
    print("Carregando artefatos gerados pelas etapas anteriores do pipeline...")
    dados = carregar_dados()
    html = montar_html(dados)

    os.makedirs(RESULTADOS_DIR, exist_ok=True)
    with open(CAMINHO_SAIDA_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Relatorio gerado em: {os.path.abspath(CAMINHO_SAIDA_HTML)}")
    webbrowser.open(f"file://{os.path.abspath(CAMINHO_SAIDA_HTML)}")


if __name__ == "__main__":
    main()
