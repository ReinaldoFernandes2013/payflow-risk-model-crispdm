PayFlow Credit Risk AI 🚀

🎯 Objetivo

Desenvolvimento de uma Inteligência Artificial robusta para prever a inadimplência de clientes (default_90d) da PayFlow, utilizando aprendizado supervisionado focado em segurança de crédito e rigor metodológico.

🔄 Metodologia: CRISP-DM

O projeto foi estruturado seguindo o framework CRISP-DM, garantindo um ciclo de vida de dados profissional:

1. Business Understanding

Alinhamento com a necessidade estratégica da PayFlow de reduzir prejuízos por inadimplência através de decisões automatizadas e céticas.

2. Data Understanding & Governança

Análise de 5.000 registros, identificando 12% de classe positiva. Abaixo, o dicionário de dados validado para este projeto:

| Nome da Coluna | Descrição | Papel no Modelo |
| :--- | :--- | :--- |
| `default_90d` | Inadimplência superior a 90 dias (0 ou 1). | **Target** |
| `score_credito` | Pontuação de risco do bureau. | Feature |
| `utilizacao_credito` | Percentual de uso do limite disponível. | Feature |
| `dias_atraso_max_12m` | Maior atraso observado nos últimos 12 meses. | Feature |
| `parcelas_pagas_ate_3m`| Dados após a concessão. | **LEAKAGE (Removido)** |
| `status_apos_90d` | Status futuro do cliente. | **LEAKAGE (Removido)** |

Nota do Investigador: A remoção de variáveis de Leakage foi crítica para evitar um modelo viciado e garantir a viabilidade no mundo real.

3. Data Preparation

Tratamento de nulos: Imputação via mediana para variáveis financeiras.

Feature Engineering: Criação da métrica comprometimento_renda.

Saneamento: Remoção rigorosa de colunas viciadas para evitar overfitting.

4. Modeling, Evaluation & Deployment
Algoritmo: Random Forest com otimização de hiperparâmetros.

Métrica Chave: Foco em Recall (0.34) para maximizar a captura de inadimplentes.

Produção: Exportação em .pkl e criação de pipeline de inferência.

🛠️ Arquitetura de Engenharia & MLOps

Data Leakage Prevention: Limpeza de variáveis que causavam métricas irreais.

Balanceamento de Classe: Implementação de SMOTE para equilibrar o aprendizado.

Qualidade de Software: Suite de testes automatizados com Pytest para validar o pipeline.

Estabilidade: Configuração otimizada para Python 3.12, evitando versões experimentais.

💻 Hardware & Benchmark (Estação de Trabalho)

Validação em ambiente de alta performance para garantir escalabilidade:CPU:
AMD Ryzen 7 9800X3D (Zen 5 Architecture).
RAM: 32GB DDR5.
Benchmark: Multiplicação de matrizes $5000 \times 5000$ em 0.3298 segundos (PyTorch).

📊 Performance Final

Recall (Inadimplentes): 0.34

F1-Score: 0.33

Principais Preditores: score_credito e comprometimento_renda.

### 📂 Estrutura do Projeto

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
source venv/Scripts/activate
pip install -r requirements.txt

2. Validar Integridade

python -m pytest
python benchmark.py

python predict.py
