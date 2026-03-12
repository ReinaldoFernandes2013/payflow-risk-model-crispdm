# PayFlow Credit Risk AI 🚀

## 🎯 Objetivo
Desenvolvimento de uma Inteligência Artificial robusta para prever a inadimplência de clientes (`default_90d`) da PayFlow, utilizando aprendizado supervisionado focado em segurança de crédito.

---

## 🔄 Metodologia: CRISP-DM
O projeto foi estruturado seguindo o framework CRISP-DM, garantindo um ciclo de vida de dados profissional:

* **Business Understanding:** Alinhamento com a necessidade da PayFlow de reduzir prejuízos por inadimplência.
* **Data Understanding:** Análise de 5.000 registros, identificando 12% de classe positiva e detecção de *Data Leakage*.
* **Data Preparation:** Tratamento de nulos via mediana e remoção de colunas viciadas.
* **Modeling:** Treinamento de Random Forest com otimização de hiperparâmetros.
* **Evaluation:** Validação focada em **Recall (0.34)**, garantindo a captura dos inadimplentes reais.

---

## 📊 Dicionário de Dados & Governança

| Nome da Coluna | Descrição | Papel no Modelo |
| :--- | :--- | :--- |
| `default_90d` | Inadimplência superior a 90 dias (0 ou 1). | **Target** |
| `score_credito` | Pontuação de risco do bureau. | Feature |
| `utilizacao_credito` | Percentual de uso do limite disponível. | Feature |
| `dias_atraso_max_12m` | Maior atraso nos últimos 12 meses. | Feature |
| `parcelas_pagas_ate_3m`| Dados após a concessão. | **LEAKAGE (Removido)** |
| `status_apos_90d` | Status futuro do cliente. | **LEAKAGE (Removido)** |

---

## 💻 Hardware & Benchmark (Estação de Trabalho)
O projeto foi validado em um ambiente de alta performance para garantir escalabilidade:
* **CPU:** AMD Ryzen 7 9800X3D (Zen 5 Architecture).
* **RAM:** 32GB DDR5.
* **Benchmark:** Multiplicação de matrizes $5000 \times 5000$ em **0.3298 segundos** utilizando PyTorch.

---

## 📂 Estrutura do Projeto

```text
├── data/                 # Base de dados (CSV)
├── models/               # Artefatos do modelo (.pkl)
├── tests/                # Testes unitários (Pytest)
├── analise_desafio.ipynb  # Notebook com documentação completa
├── predict.py            # Script de produção/inferência
├── benchmark.py          # Script de validação de hardware
├── requirements.txt      # Dependências do projeto
└── .gitignore            # Filtro de arquivos para o Git

🚀 Como executar?
1. Configurar Ambiente

python -m venv venv
source venv/Scripts/activate  # No Windows use: venv\Scripts\activate
pip install -r requirements.txt

2. Validar Integridade (Testes & Hardware)

python -m pytest
python benchmark.py

python predict.py

