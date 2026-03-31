
# 📊 TECH CHALLENGE AI: Estratégia de Retenção e Experiência do Cliente

**Grupo:** Reinaldo Fernandes (RM371717), Leonardo Gonzales (RM373713), Winny Tavares (RM371471)
**Projeto:** Tech Challenge Fase 1 - Pós-Graduação AI Scientist (FIAP)

## 🎯 1. Entendimento de Negócio (CRISP-DM)

O **PayFlow AI** é um sistema de inteligência antecipatória desenvolvido para mitigar a natureza reativa do NPS tradicional. Em vez de esperar o cliente reclamar, nossa solução identifica padrões de comportamento logístico e de atendimento que precedem a insatisfação.

### Por que o NPS é crítico para o nosso E-commerce?

1. **Proteção de Receita (LTV):** Provamos matematicamente que clientes satisfeitos possuem **57% mais chances de recompra** em 30 dias.
2. **Redução de CAC:** Promotores reduzem o custo de aquisição através do marketing orgânico.
3. **Eficiência Operacional:** Identificar um detrator proativamente custa menos do que tentar recuperar um cliente que já abandonou a marca.

**Pergunta Norteadora:** *"Quais fricções operacionais e logísticas são capazes de converter um potencial promotor em um detrator antes mesmo da entrega ser concluída?"*

## 🔬 2. Diagnóstico e Storytelling com Dados (EDA)

Nossa análise exploratória evoluiu de uma observação técnica para um diagnóstico de causas raiz:

* **O Ponto de Ruptura:** Identificamos que a tolerância do nosso cliente ao atraso é  **nula (0 dias)** . A partir do momento em que a promessa de entrega é quebrada, a probabilidade de detração ultrapassa 50%.
* **A Fricção do Suporte:** Clientes insatisfeitos exigem **140% mais esforço** do time de atendimento (média de 1.63 contatos vs 0.67 de promotores).
* **Rigor Científico:** Através do teste de hipótese  **Mann-Whitney U** , provamos com 95% de confiança que o atraso logístico é o principal causador da queda de satisfação, eliminando a possibilidade de flutuações aleatórias.

## 🤖 3. O "Escudo de Retenção" (Modelo Preditivo)

Desenvolvemos um motor de classificação binária baseado em  **Random Forest** , focado em sensibilidade operacional:

* **Performance:** AUC-ROC de  **0.92** , demonstrando alta robustez.
* **Recall de 100%:** O modelo foi calibrado para não deixar nenhum potencial detrator passar despercebido.
* **Feature Importance:** As variáveis que mais "pesam" na predição são o histórico de recompra, o volume de reclamações e o **delay_ratio** (Índice de Frustração Relativa).

## 🚀 4. Recomendações Práticas e Plano de Ação

Com base nos insights, propomos três ações imediatas para a diretoria:

1. **Alerta de Atraso Zero:** Implementação de um gatilho prioritário na logística para pedidos que atinjam 24h de atraso, disparando notificação proativa ao cliente.
2. **Voucher de Reversão:** Automação de envio de compensação (voucher/frete grátis) para clientes identificados pela IA como "Risco Crítico" antes mesmo da abertura de reclamação.
3. **Priorização no SAC:** Integração do "Escore de Risco" no dashboard de atendimento, permitindo que a linha de frente priorize casos com alta probabilidade de detração.

## 🛡️ 5. Governança e Limitações

* **Rigor de QA:** O sistema conta com testes de estresse que validam a reação da IA em cenários de crise logística extrema.
* **Limitações:** O modelo depende da integridade dos logs de transporte. Recomendamos retreinamento trimestral para capturar mudanças de comportamento em datas sazonais (Black Friday).

## ⚙️ Como Executar

1. **Instalar Dependências:** `pip install -r requirements.txt`
2. **Executar Diagnóstico:** `python src/predict_tech_challenge.py`
3. **Dashboard Executivo:** `streamlit run src/app_tech_challenge.py`
4. **Auditoria de Qualidade:** `pytest tests/test_tech_challenge.py -v`

*Este projeto demonstra a capacidade técnica do grupo em transformar dados brutos em decisões estratégicas de alto impacto.*
