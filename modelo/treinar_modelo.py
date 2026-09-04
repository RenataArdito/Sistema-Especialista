"""
treinar_modelo.py
==================
Terceira etapa do pipeline (Implementacao do modelo, conforme o
diagrama de arquitetura do artigo):
  Base de Dados -> Divisao 80/20 -> Treino Random Forest / Teste
  -> Avaliacao (F1-score etc) -> Modelo Treinado

Carrega a matriz de features (dataset_features.csv), separa
treino/teste com estratificacao por classe (80/20, igual ao artigo),
treina um RandomForestClassifier e avalia com accuracy, precision,
recall e F1-score (por classe e macro/weighted), conforme a
metodologia descrita no artigo. Gera tambem a matriz de confusao e o
grafico de importancia das features.

Alem disso, treina 3 modelos baseline (classificador de maioria,
regressao logistica e KNN) sobre o MESMO split e as MESMAS features,
para contextualizar se o desempenho do Random Forest e' de fato
superior a alternativas simples -- comparacao que o relatorio final
(gerado por relatorio/gerar_relatorio.py) exibe lado a lado.

Uso:
    python3 treinar_modelo.py
Gera (em ../resultados/):
    modelo_random_forest.joblib
    classification_report.txt
    confusion_matrix.png
    feature_importance.png
    metricas_resumo.csv
    comparacao_modelos.json
"""

import json
import os

import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
ENTRADA_CSV = os.path.join(BASE_DIR, "resultados", "dataset_features.csv")
DIR_RESULTADOS = os.path.join(BASE_DIR, "resultados")

COLUNAS_NAO_FEATURE = {"id", "algoritmo", "categoria", "codigo_limpo"}

RANDOM_STATE = 42


def carregar_dados():
    df = pd.read_csv(ENTRADA_CSV)
    colunas_features = [c for c in df.columns if c not in COLUNAS_NAO_FEATURE]
    X = df[colunas_features]
    y = df["categoria"]
    return df, X, y, colunas_features


def main():
    df, X, y, colunas_features = carregar_dados()
    print(f"Total de exemplos: {len(df)}")
    print(f"Total de atributos (features): {len(colunas_features)}")
    print(f"Classes: {sorted(y.unique())}")

    codificador = LabelEncoder()
    y_codificado = codificador.fit_transform(y)

    # Divisao 80/20 estratificada por classe, igual ao diagrama de
    # arquitetura do artigo (Conjunto Treino 80% / Conjunto Teste 20%)
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y_codificado,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y_codificado,
    )
    print(f"\nConjunto de treino: {len(X_treino)} exemplos")
    print(f"Conjunto de teste : {len(X_teste)} exemplos")

    # Treinamento do modelo Random Forest (algoritmo definido no artigo)
    # n_jobs=1 (em vez de -1): com apenas 420 exemplos o treino e' quase
    # instantaneo de qualquer forma, e manter um unico worker evita que a
    # agregacao de votos das arvores varie por ponto flutuante entre
    # maquinas com numero de nucleos diferente, garantindo que qualquer
    # pessoa que rode este script obtenha exatamente as mesmas metricas
    # relatadas no Relatorio_Implementacao.docx.
    modelo = RandomForestClassifier(
        n_estimators=300,
        max_depth=None,
        min_samples_leaf=1,
        random_state=RANDOM_STATE,
        n_jobs=1,
        class_weight="balanced",
    )
    modelo.fit(X_treino, y_treino)

    # Validacao cruzada (5-fold) no conjunto de treino, para checar
    # estabilidade do modelo alem da divisao 80/20 unica
    scores_cv = cross_val_score(modelo, X_treino, y_treino, cv=5, scoring="f1_macro")
    print(f"\nValidacao cruzada (5-fold, F1-macro no treino): "
          f"{scores_cv.mean():.4f} +/- {scores_cv.std():.4f}")

    # Avaliacao no conjunto de teste (20% nunca visto pelo modelo)
    y_pred = modelo.predict(X_teste)

    acuracia = accuracy_score(y_teste, y_pred)
    precisao_macro = precision_score(y_teste, y_pred, average="macro", zero_division=0)
    recall_macro = recall_score(y_teste, y_pred, average="macro", zero_division=0)
    f1_macro = f1_score(y_teste, y_pred, average="macro", zero_division=0)
    f1_weighted = f1_score(y_teste, y_pred, average="weighted", zero_division=0)

    print("\n===== METRICAS NO CONJUNTO DE TESTE (20%) =====")
    print(f"Acuracia            : {acuracia:.4f}")
    print(f"Precisao (macro)    : {precisao_macro:.4f}")
    print(f"Recall (macro)      : {recall_macro:.4f}")
    print(f"F1-score (macro)    : {f1_macro:.4f}")
    print(f"F1-score (weighted) : {f1_weighted:.4f}")

    relatorio_texto = classification_report(
        y_teste, y_pred, target_names=codificador.classes_, zero_division=0
    )
    print("\n" + relatorio_texto)

    os.makedirs(DIR_RESULTADOS, exist_ok=True)

    # ------------------------------------------------------------------
    # Baselines de comparacao: sem eles, nao ha como saber se 54,8% de
    # acuracia e' um resultado forte, fraco ou equivalente ao de um
    # classificador trivial. Treinados sobre o MESMO split 80/20 e as
    # MESMAS 25 features do Random Forest, para comparacao justa.
    # Regressao Logistica e KNN recebem as features padronizadas
    # (media 0, desvio 1); o Random Forest e o Dummy nao precisam disso.
    # ------------------------------------------------------------------
    escalador = StandardScaler()
    X_treino_esc = escalador.fit_transform(X_treino)
    X_teste_esc = escalador.transform(X_teste)

    candidatos_baseline = [
        ("Maioria (Dummy)", DummyClassifier(strategy="most_frequent", random_state=RANDOM_STATE), X_treino, X_teste),
        ("Regressao Logistica", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE), X_treino_esc, X_teste_esc),
        ("KNN (k=5)", KNeighborsClassifier(n_neighbors=5), X_treino_esc, X_teste_esc),
    ]

    comparacao_modelos = [{
        "modelo": "Random Forest",
        "acuracia": acuracia,
        "precisao_macro": precisao_macro,
        "recall_macro": recall_macro,
        "f1_macro": f1_macro,
    }]

    print("\n===== COMPARACAO COM MODELOS BASELINE (mesmo split e features) =====")
    print(f"{'Modelo':22s} {'Acuracia':>10s} {'Prec.macro':>12s} {'Rec.macro':>11s} {'F1 macro':>10s}")
    print(f"{'Random Forest':22s} {acuracia:10.4f} {precisao_macro:12.4f} {recall_macro:11.4f} {f1_macro:10.4f}")

    for nome, modelo_base, X_tr, X_te in candidatos_baseline:
        modelo_base.fit(X_tr, y_treino)
        y_pred_base = modelo_base.predict(X_te)
        acc_b = accuracy_score(y_teste, y_pred_base)
        prec_b = precision_score(y_teste, y_pred_base, average="macro", zero_division=0)
        rec_b = recall_score(y_teste, y_pred_base, average="macro", zero_division=0)
        f1_b = f1_score(y_teste, y_pred_base, average="macro", zero_division=0)
        comparacao_modelos.append({
            "modelo": nome,
            "acuracia": acc_b,
            "precisao_macro": prec_b,
            "recall_macro": rec_b,
            "f1_macro": f1_b,
        })
        print(f"{nome:22s} {acc_b:10.4f} {prec_b:12.4f} {rec_b:11.4f} {f1_b:10.4f}")

    with open(os.path.join(DIR_RESULTADOS, "comparacao_modelos.json"), "w", encoding="utf-8") as f:
        json.dump(comparacao_modelos, f, ensure_ascii=False, indent=2)

    # salva relatorio de classificacao completo
    caminho_relatorio = os.path.join(DIR_RESULTADOS, "classification_report.txt")
    with open(caminho_relatorio, "w", encoding="utf-8") as f:
        f.write("RELATORIO DE CLASSIFICACAO - CONJUNTO DE TESTE (20%)\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Acuracia            : {acuracia:.4f}\n")
        f.write(f"Precisao (macro)    : {precisao_macro:.4f}\n")
        f.write(f"Recall (macro)      : {recall_macro:.4f}\n")
        f.write(f"F1-score (macro)    : {f1_macro:.4f}\n")
        f.write(f"F1-score (weighted) : {f1_weighted:.4f}\n")
        f.write(f"Validacao cruzada 5-fold (F1-macro, treino): "
                f"{scores_cv.mean():.4f} +/- {scores_cv.std():.4f}\n\n")
        f.write(relatorio_texto)
        f.write("\n\nCOMPARACAO COM BASELINES (mesmo split e features)\n")
        f.write("-" * 60 + "\n")
        for item in comparacao_modelos:
            f.write(f"  {item['modelo']:22s}: acuracia={item['acuracia']:.4f}  "
                     f"f1_macro={item['f1_macro']:.4f}\n")

    # salva metricas resumidas em CSV (util para o relatorio)
    pd.DataFrame([{
        "acuracia": acuracia,
        "precisao_macro": precisao_macro,
        "recall_macro": recall_macro,
        "f1_macro": f1_macro,
        "f1_weighted": f1_weighted,
        "cv_f1_macro_media": scores_cv.mean(),
        "cv_f1_macro_desvio": scores_cv.std(),
        "n_treino": len(X_treino),
        "n_teste": len(X_teste),
        "n_features": len(colunas_features),
    }]).to_csv(os.path.join(DIR_RESULTADOS, "metricas_resumo.csv"), index=False)

    # ---- Matriz de confusao ----
    matriz = confusion_matrix(y_teste, y_pred)
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(
        matriz, annot=True, fmt="d", cmap="Blues",
        xticklabels=codificador.classes_, yticklabels=codificador.classes_, ax=ax
    )
    ax.set_xlabel("Categoria prevista")
    ax.set_ylabel("Categoria real")
    ax.set_title("Matriz de Confusao - Random Forest (conjunto de teste)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(DIR_RESULTADOS, "confusion_matrix.png"), dpi=150)
    plt.close(fig)

    # ---- Importancia das features ----
    importancias = pd.Series(modelo.feature_importances_, index=colunas_features)
    importancias = importancias.sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(9, 8))
    importancias.plot(kind="barh", ax=ax, color="#3B6FA0")
    ax.set_xlabel("Importancia (Gini / MDI)")
    ax.set_title("Importancia das Features - Random Forest")
    plt.tight_layout()
    plt.savefig(os.path.join(DIR_RESULTADOS, "feature_importance.png"), dpi=150)
    plt.close(fig)

    # ---- Salva o modelo treinado + metadados necessarios para inferencia ----
    pacote = {
        "modelo": modelo,
        "codificador_rotulos": codificador,
        "colunas_features": colunas_features,
    }
    joblib.dump(pacote, os.path.join(DIR_RESULTADOS, "modelo_random_forest.joblib"))

    print(f"\nArtefatos salvos em: {os.path.abspath(DIR_RESULTADOS)}")
    print(" - modelo_random_forest.joblib")
    print(" - classification_report.txt")
    print(" - metricas_resumo.csv")
    print(" - comparacao_modelos.json")
    print(" - confusion_matrix.png")
    print(" - feature_importance.png")


if __name__ == "__main__":
    main()
