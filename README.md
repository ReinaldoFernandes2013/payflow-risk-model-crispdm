# PayFlow Credit Risk AI 🚀

## 🎯 Objetivo
Desenvolvimento de uma Inteligência Artificial robusta para prever a inadimplência de clientes (`default_90d`) da PayFlow, utilizando aprendizado supervisionado focado em segurança de crédito.

---

## 🔄 Metodologia: CRISP-DM
O projeto foi estruturado seguindo o framework **CRISP-DM**, garantindo um ciclo de vida de dados profissional:



1.  **Business Understanding**: Alinhamento com a necessidade da PayFlow de reduzir prejuízos por inadimplência.
2.  **Data Understanding**: Análise de 5.000 registros, identificando 12% de classe positiva e detecção de *Data Leakage*.
3.  **Data Preparation**: 
    * Tratamento de nulos via mediana.
    * **Feature Engineering**: Criação da métrica `comprometimento_renda`.
    * Remoção de colunas viciadas para evitar overfitting.
4.  **Modeling**: Treinamento de **Random Forest** com otimização de hiperparâmetros.
5.  **Evaluation**: Validação focada em **Recall**, garantindo a captura dos inadimplentes reais.
6.  **Deployment**: Exportação do modelo em `.pkl` e criação de script de inferência.

---

## 🛠️ Arquitetura de Engenharia & MLOps
* **Data Leakage Prevention**: Limpeza rigorosa de variáveis de atraso que causavam métricas irreais.
* **Balanceamento de Classe**: Implementação de **SMOTE** para equilibrar o aprendizado do modelo.
* **Qualidade de Software**: Suite de testes automatizados com **Pytest** para validar o carregamento do modelo e o pipeline de entrada.



## 📊 Performance Final
* **Recall (Inadimplentes)**: 0.34
* **F1-Score**: 0.33
* **Variáveis Principais**: `score_credito` e `comprometimento_renda`.

---

## 📂 Estrutura do Projeto
```text
├── data/               # Base de dados (CSV)
├── models/             # Artefatos do modelo (.pkl)
├── tests/              # Testes unitários (Pytest)
├── analise_desafio.ipynb # Notebook com documentação completa
├── predict.py          # Script de produção/inferência
├── requirements.txt    # Dependências do projeto
└── .gitignore          # Filtro de arquivos para o Git

🚀 Como executar?
Configurar Ambiente:

python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

Validar Integridade (Testes):

python -m pytest

Realizar Predição:

python predict.py

