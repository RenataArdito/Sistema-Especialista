# 🔎 Sistema Especialista para Classificação de Defeitos de Software

> Implementação prática de um **sistema especialista baseado em Machine Learning** para apoiar a inspeção de código-fonte e a classificação automática de defeitos, desenvolvido como Trabalho de Conclusão de Curso (TCC) na **Universidade Presbiteriana Mackenzie**.

O projeto reproduz, de ponta a ponta, a arquitetura proposta no artigo *"Sistema Especialista Baseado em Machine Learning para Auxílio na Inspeção de Código Fonte e Classificação de Defeitos de Software"*: construção da base de dados, pré-processamento e extração de atributos via AST, treinamento de um classificador **Random Forest** e inferência sobre código novo — seguindo exatamente o diagrama de arquitetura descrito na Seção 3 do artigo.

📄 Documentação completa (decisões de projeto, resultados e limitações): [`Relatorio_Implementacao.docx`](Relatorio_Implementacao.docx)

---

## Sumário

- [Visão geral](#visão-geral)
- [Arquitetura do pipeline](#arquitetura-do-pipeline)
- [Base de dados](#base-de-dados)
- [Resultados](#resultados)
- [Como executar](#como-executar)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Principais decisões de projeto](#principais-decisões-de-projeto)
- [Tecnologias](#tecnologias)
- [Autoria](#autoria)

---

## Visão geral

Revisão manual de código é cara, lenta e sujeita a viés do revisor. Este projeto investiga se um modelo de aprendizado de máquina, treinado sobre atributos estruturais e sintáticos extraídos da **árvore sintática abstrata (AST)** do código, consegue **classificar automaticamente a categoria de um defeito** — funcionando como um "primeiro filtro" especialista que direciona a atenção do revisor humano.

O sistema classifica cada trecho de código em uma de **7 categorias de defeito**, inspiradas na taxonomia de mutação de software (Mutation Testing, DeMillo et al., 1978):

| Categoria | Descrição |
|---|---|
| `inicializacao` | Variáveis inicializadas com valor incorreto |
| `controle` | Condições de laço/decisão alteradas (limites, operadores) |
| `dados` | Estruturas de dados manipuladas incorretamente |
| `computacao` | Operadores aritméticos/lógicos trocados |
| `comissao` | Instrução ou operação trocada por outra (ex.: `min()` no lugar de `max()`) |
| `excesso` | Código redundante ou operações desnecessárias |
| `desempenho` | Implementação correta, porém ineficiente |

## Arquitetura do pipeline

```
   dados/erros.py                  preprocessamento/            modelo/                    inferencia/
 ┌───────────────────┐      ┌───────────────────────┐   ┌──────────────────────┐   ┌──────────────────────────┐
 │ 420 funções        │      │ Limpeza anti-vazamento │   │ Random Forest         │   │ Código novo               │
 │ (10 algoritmos ×    │ ──▶ │ de rótulo + extração   │──▶│ (split 80/20,         │──▶│ → mesmo pré-processamento │
 │  7 categorias ×     │      │ de 25 features via AST │   │  validação cruzada)   │   │ → classificação           │
 │  6 variantes)       │      └───────────────────────┘   └──────────────────────┘   └──────────────────────────┘
 └───────────────────┘
```

Cada etapa é um script Python independente e auditável isoladamente; `executar_pipeline.py` apenas orquestra a execução das quatro etapas na ordem do diagrama, sem duplicar lógica.

## Base de dados

- **420 exemplos rotulados**, gerados a partir de **10 algoritmos clássicos** (média, ordenação, busca linear/binária, fatorial, reversão de string, média ponderada, bubble sort, Fibonacci, contagem de vogais) × **7 categorias de defeito** × **6 variantes** cada, mais 10 versões corretas de referência.
- Metodologia de mutação controlada, garantindo rótulos balanceados (60 exemplos por categoria) e rastreáveis à definição da Tabela 2 do artigo.
- **25 atributos numéricos** extraídos via AST: contagem de laços, condicionais, operadores aritméticos/relacionais/lógicos, chamadas recursivas, profundidade máxima de aninhamento, razões estruturais, entre outros.
- Roteiro documentado (`dados/integracao_quixbugs.py`) para complementar a base com o dataset público **QuixBugs** (Lin, Koppel et al., 2017) — usado apenas como referência, não entra no treinamento atual.

## Resultados

Avaliação sobre o conjunto de teste (20%, 84 exemplos), modelo Random Forest:

| Métrica | Valor |
|---|---|
| Acurácia | **54,8%** |
| Precisão (macro) | 58,1% |
| Recall (macro) | 54,8% |
| F1-score (macro) | 53,9% |
| F1-score (weighted) | 53,9% |
| Validação cruzada 5-fold (F1-macro, treino) | 44,5% ± 3,2% |

**Desempenho por categoria** (precisão / recall / F1):

| Categoria | Precisão | Recall | F1 |
|---|---|---|---|
| `inicializacao` | 0.90 | 0.75 | **0.82** |
| `controle` | 0.82 | 0.75 | 0.78 |
| `computacao` | 0.50 | 0.75 | 0.60 |
| `excesso` | 0.43 | 0.75 | 0.55 |
| `comissao` | 0.80 | 0.33 | 0.47 |
| `dados` | 0.40 | 0.33 | 0.36 |
| `desempenho` | 0.22 | 0.17 | 0.19 |

As categorias com maior sinal estrutural (`inicializacao`, `controle`) — que alteram diretamente o AST — são as mais bem classificadas. Já `desempenho` (código correto, porém ineficiente) é a mais difícil, pois não introduz nenhuma mudança estrutural detectável pelas features atuais — uma limitação discutida em detalhe no relatório técnico.

Gráficos gerados automaticamente pelo pipeline:

| Matriz de confusão | Importância das features |
|---|---|
| `resultados/confusion_matrix.png` | `resultados/feature_importance.png` |

## Como executar

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

### Opção 1 — um único comando (recomendado)

```bash
python executar_pipeline.py
```

Roda as 4 etapas em sequência (construção da base → pré-processamento → treino/avaliação do modelo → inferência sobre código novo), na ordem exata do diagrama de arquitetura do artigo. Ao final, imprime o resumo das métricas no terminal e abre a matriz de confusão e o gráfico de importância das features.

### Opção 2 — passo a passo (para auditar/estudar cada etapa isoladamente)

```bash
# 1) Construção da base de dados a partir de dados/erros.py
cd dados
python construir_dataset.py
# -> gera ../resultados/dataset_codigos.csv (420 exemplos, 60 por categoria)

# 2) Pré-processamento e extração de features (AST)
cd ../preprocessamento
python preprocessamento.py
# -> gera ../resultados/dataset_features.csv (25 atributos numéricos)

# 3) Treinamento e avaliação do modelo Random Forest
cd ../modelo
python treinar_modelo.py
# -> gera modelo_random_forest.joblib, classification_report.txt,
#    confusion_matrix.png, feature_importance.png, metricas_resumo.csv

# 4) Classificação de código novo (demonstração ponta a ponta)
cd ../inferencia
python classificar_codigo.py
```

## Estrutura de pastas

```
executar_pipeline.py        -> ponto de entrada único: roda as 4 etapas em sequência

dados/
  erros.py                  -> base de dados sintética: 420 funções com defeito
                                (10 algoritmos x 7 categorias x 6 variantes)
                                + 10 versões corretas de referência
  construir_dataset.py      -> extrai o código-fonte de erros.py e monta o CSV rotulado
  integracao_quixbugs.py    -> roteiro documentado para complementar a base com o
                                dataset público QuixBugs (Lin, Koppel et al., 2017)
  QuixBugs/                 -> (opcional) clone do dataset público QuixBugs,
                                usado apenas como referência para a integração
                                descrita em integracao_quixbugs.py — não entra
                                no treinamento do modelo

preprocessamento/
  preprocessamento.py       -> limpeza anti-vazamento de rótulo + extração de
                                25 features estruturais/sintáticas via AST

modelo/
  treinar_modelo.py         -> divisão 80/20 estratificada, treino Random Forest,
                                validação cruzada, métricas e gráficos

inferencia/
  classificar_codigo.py     -> pipeline de inferência completo (novo código ->
                                pré-processamento -> features -> classificação)

resultados/                 -> gerado ao rodar os 3 primeiros scripts, nesta ordem
  dataset_codigos.csv          -> 420 exemplos rotulados (id, algoritmo, categoria, código)
  dataset_features.csv         -> matriz de features numéricas + rótulo
  modelo_random_forest.joblib  -> modelo treinado, pronto para uso
  classification_report.txt / metricas_resumo.csv -> métricas de avaliação
  confusion_matrix.png / feature_importance.png    -> gráficos de avaliação

Relatorio_Implementacao.docx -> relatório técnico completo (o que foi feito, como e por quê)
```

## Principais decisões de projeto

> Detalhes completos de cada decisão, com justificativa, no relatório técnico.

1. **Categoria "Comissão" do arquivo original foi reescrita.** O arquivo enviado continha, nessa categoria, erros de *omissão* (checagens/retornos ausentes), o que diverge da definição da Tabela 2 do artigo. A nova versão representa trocas de instrução/operação (ex.: `min()` no lugar de `max()`).
2. **420 exemplos, 60 por categoria**, gerados a partir de 10 algoritmos × 7 categorias × 6 variantes, seguindo uma metodologia de mutação inspirada em Mutation Testing (DeMillo et al., 1978).
3. **Anti-vazamento de rótulo**: nomes de função e comentários que indicavam a categoria são removidos antes da extração de features.
4. **Random Forest, divisão 80/20, métricas de acurácia/precisão/recall/F1**, exatamente como especificado no artigo.

## Tecnologias

`Python` · `pandas` · `NumPy` · `scikit-learn` (Random Forest) · `matplotlib` / `seaborn` · `AST` (análise estática de código) · `joblib`

## Autoria

Trabalho de Conclusão de Curso — Universidade Presbiteriana Mackenzie
**Renata Ardito**
