
# 🌍 Inteligência Territorial: Processamento e Auditoria IDHM

Este módulo faz parte do ecossistema **PayFlow** e tem como objetivo transformar dados brutos do Índice de Desenvolvimento Humano Municipal (IDHM 2010) em inteligência acionável para a expansão de produtos de crédito e análise de mercado de alto padrão.

## 🎯 Objetivo

Implementar um pipeline robusto de **ETL (Extract, Load, Transform)** e **Auditoria de Dados** com foco em identificar  **Territórios Premium** , garantindo o rigor técnico para modelos de Machine Learning e tomadas de decisão estratégica.

## 🏗️ Arquitetura do Módulo

O projeto segue uma estrutura modular e escalável, aderente aos princípios de MLOps:

* `src/idhm.py`: O "motor" de processamento. Contém a lógica de localização, limpeza, **classificação de status** e auditoria.
* `tests/test_idhm.py`: Suite de testes unitários para garantir a integridade da lógica de negócio.
* `src/app_idhm.py`: Interface interativa (Streamlit) com foco em UX/UI para visualização de indicadores e clusters de mercado.

## ⚙️ Funcionalidades Técnicas

### 1. Pipeline de ETL & Business Logic (idhm.py)

O motor de processamento realiza operações avançadas de engenharia de dados:

* **Normalização de Schema** : Padronização de cabeçalhos para `snake_case`.
* **Seleção Estratégica** : Filtra as dimensões críticas (Educação, Longevidade e Renda).
* **Classificação Automática (Status)** : Implementação de regra de negócio que rotula municípios como `✅ Premium` (IDHM ≥ 0.7) ou `⚠️ Em Desenvolvimento` (IDHM < 0.7).
* **Tipagem Forte** : Conversão forçada para tipos numéricos, evitando falhas em cálculos estatísticos.

### 2. Auditoria de Qualidade (Data Quality Gatekeeper)

A função `run_data_audit` valida a integridade técnica antes de qualquer análise:

* **Schema** : Verificação obrigatória da presença das features e da nova coluna de `status`.
* **Integridade** : Zero tolerância para valores nulos no indicador principal.
* **Domínio** : Validação matemática da escala do IDH (entre 0 e 1).
* **Geografia** : Consistência das 27 Unidades Federativas do Brasil.

## 🧪 Validação e Testes (Pytest)

A robustez da solução é garantida por testes automatizados que validam a lógica de negócio e a estabilidade do código.

**Comando para execução:**

**Bash**

```
pytest tests/test_idhm.py -v
```

**Principais Testes:**

* `test_file_discovery`: Valida a localização dinâmica dos dados.
* `test_data_cleaning_and_status_logic`: Garante que a classificação de municípios (Premium vs Desenvolvimento) está operando conforme a meta de 0.7.
* `test_audit_integrity`: Validação rigorosa dos limites matemáticos da base.
* `test_numeric_consistency`: Assegura a integridade dos tipos de dados para análise.

## 📊 Dashboard Interativo (Streamlit)

Interface de Business Intelligence com foco em identificar oportunidades:

* **Filtros Estratégicos** : Seleção por UF, Status de Mercado e piso de IDH (Default: 0.7).
* **Gráficos Premium** :
* **Ranking de Potencial de Renda** : Identificação do Top 15 cidades para conversão.
* **Matriz de Decisão (Scatter Plot)** : Visualização da correlação Renda vs Educação com linha de meta.
* **Métricas Dinâmicas** : Resumo instantâneo de Ticket Médio e Nível Educacional da amostra filtrada.

**Bash**

```
streamlit run src/app_idhm.py
```

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Pandas** : Manipulação e transformação de dados de alta performance.
* **Plotly** : Visualizações interativas e científicas.
* **Streamlit** : Framework para deployment de Data Apps.
* **Pytest** : Framework de testes para garantia de qualidade (QA).

---

**Nota de Rigor Científico:** Este módulo utiliza uma régua de corte fundamentada estatisticamente (IDHM 0.700), permitindo que a organização foque recursos nos territórios com maior maturidade socioeconômica e menor risco de crédito.
