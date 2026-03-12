# PayFlow Credit Risk AI 🚀

## 🎯 Objetivo
Desenvolvimento de uma Inteligência Artificial robusta para prever a inadimplência de clientes (`default_90d`) da PayFlow, utilizando aprendizado supervisionado focado em segurança de crédito.

---

## 🔄 Metodologia: CRISP-DM
O projeto segue o framework CRISP-DM para garantir um ciclo de vida de dados profissional:

* **Business Understanding:** Redução de prejuízos operacionais por inadimplência.
* **Data Understanding:** Análise de 5.000 registros com identificação de *Data Leakage*.
* **Data Preparation:** Imputação de nulos e saneamento de variáveis viciadas.
* **Modeling:** Implementação de Random Forest Classifier.
* **Evaluation:** Foco na métrica **Recall (0.34)**.

---

## 📊 Dicionário de Dados & Governança

| Nome da Coluna | Descrição | Papel no Modelo |
| :--- | :--- | :--- |
| `default_90d` | Inadimplência superior a 90 dias. | **Target** |
| `score_credito` | Pontuação de risco do bureau. | Feature |
| `utilizacao_credito` | Percentual de uso do limite. | Feature |
| `parcelas_pagas_ate_3m`| Dados após a concessão. | **LEAKAGE (Removido)** |

---

## 💻 Hardware & Benchmark
* **CPU:** AMD Ryzen 7 9800X3D
* **RAM:** 32GB DDR5
* **Benchmark:** Matrizes $5000 \times 5000$ em **0.32s**.

---

## 📂 Estrutura do Projeto

```text
├── data/                 # Base de dados (CSV)
├── models/               # Artefatos do modelo (.pkl)
├── predict.py            # Script de produção/inferência
├── benchmark.py          # Script de validação de hardware
└── requirements.txt      # Dependências do projeto


🚀 Como executar?

1. Configurar Ambiente

python -m venv venv
source venv/Scripts/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Validar Integridade

python -m pytest
python benchmark.py

3. Realizar Predição

python predict.py