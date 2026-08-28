# Sistema Especialista — Implementação

Implementação prática da metodologia descrita no artigo *"Sistema
Especialista Baseado em Machine Learning para Auxílio na Inspeção de
Código Fonte e Classificação de Defeitos de Software"*: construção da
base de dados, pré-processamento, treinamento de um classificador
Random Forest e inferência sobre código novo, seguindo exatamente o
diagrama de arquitetura da Seção 3 do artigo.

Veja `Relatorio_Implementacao.docx` para a documentação completa de
cada decisão tomada, dos resultados obtidos e das limitações
identificadas.

## Como executar

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

### Opção 1 — um único comando (recomendado)

```bash
python executar_pipeline.py
```

Roda as 4 etapas em sequência (construção da base → pré-processamento →
treino/avaliação do modelo → inferência sobre código novo), exatamente
na ordem do diagrama de arquitetura do artigo, chamando os mesmos 4
scripts abaixo — não duplica nenhuma lógica, só orquestra a execução.
Ao final, imprime o resumo das métricas no terminal e abre a matriz de
confusão e o gráfico de importância das features para visualização.

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

## Principais decisões (resumo — detalhes no relatório)

1. **Categoria "Comissão" do arquivo original foi reescrita.** O arquivo enviado
   continha, nessa categoria, erros de *omissão* (checagens/retornos ausentes),
   o que diverge da definição da Tabela 2 do artigo. A nova versão representa
   trocas de instrução/operação (ex.: `min()` no lugar de `max()`).
2. **420 exemplos, 60 por categoria**, gerados a partir de 10 algoritmos (os
   mesmos do arquivo original) × 7 categorias × 6 variantes, seguindo uma
   metodologia de mutação inspirada em Mutation Testing (DeMillo et al., 1978).
3. **Anti-vazamento de rótulo**: nomes de função e comentários que indicavam a
   categoria são removidos antes da extração de features.
4. **Random Forest, divisão 80/20, métricas de acurácia/precisão/recall/F1**,
   exatamente como especificado no artigo.
