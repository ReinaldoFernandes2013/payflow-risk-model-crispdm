import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import os

def predict_customer_satisfaction(input_data):
    """
    Motor de Predição de NPS (PayFlow AI - Tech Challenge)
    Converte dados operacionais em alertas de risco e recomendações de negócio.
    """
    
    # --- 1. CONFIGURAÇÃO DE CAMINHOS (MLOps Robustness) ---
    current_dir = Path(__file__).resolve().parent
    root_path = current_dir.parent if current_dir.name == 'src' else current_dir
    
    model_path = root_path / "models" / "modelo_nps_rf.pkl"
    features_path = root_path / "models" / "features_nps.pkl"
    
    # Validação de ativos
    if not model_path.exists() or not features_path.exists():
        return {
            "status": "Erro",
            "mensagem": "Ativos de IA (model/features) não encontrados na pasta /models."
        }

    try:
        # --- 2. CARGA DOS ATIVOS CERTIFICADOS ---
        model = joblib.load(model_path)
        features_treino = joblib.load(features_path)
        
        # --- 3. PREPARAÇÃO DOS DADOS (Storytelling Input) ---
        df_input = pd.DataFrame([input_data])

        # Sincronização da Engenharia de Features (Índice de Frustração Relativa)
        if 'delivery_delay_days' in df_input.columns and 'delivery_time_days' in df_input.columns:
            # Cálculo do ratio para capturar a percepção temporal do cliente
            df_input['delay_ratio'] = df_input['delivery_delay_days'] / (df_input['delivery_time_days'] + 1)
        
        # Alinhamento de Dimensões (Garante que o modelo receba as colunas exatas do treino)
        df_final = pd.DataFrame(0, index=[0], columns=features_treino)
        for col in df_input.columns:
            if col in df_final.columns:
                df_final[col] = df_input[col].values

        # --- 4. EXECUÇÃO DA INTELIGÊNCIA ---
        # Calculamos a probabilidade para permitir uma tomada de decisão granular
        prob_detracao = model.predict_proba(df_final)[:, 1][0]
        
        # --- 5. LÓGICA DE NEGÓCIO E RECOMENDAÇÕES (Feedback Prof. Alexandre) ---
        # Ponto de Ruptura Logística identificado no Notebook: 3 dias
        dias_atraso = input_data.get('delivery_delay_days', 0)
        ponto_ruptura_atingido = dias_atraso >= 3
        
        # Definição de Status Executivo
        if prob_detracao > 0.70:
            nivel_risco = "CRÍTICO (Ação Imediata)"
            recomendacao = "Disparar Voucher de Compensação e priorizar contato humano (SAC Nível 3)."
        elif prob_detracao > 0.35:
            nivel_risco = "MODERADO (Alerta Preventivo)"
            recomendacao = "Enviar notificação push explicativa e monitorar próxima etapa logística."
        else:
            nivel_risco = "BAIXO (Potencial Promotor)"
            recomendacao = "Oportunidade de Cross-selling ou convite para programa de fidelidade."

        return {
            "status": "Sucesso",
            "diagnostico": nivel_risco,
            "probabilidade_detracao": f"{prob_detracao:.1%}",
            "insight_logistico": "Ponto de Ruptura Atingido" if ponto_ruptura_atingido else "Dentro da Tolerância",
            "plano_de_acao": recomendacao,
            "metrica_apoio": {
                "dias_atraso": dias_atraso,
                "escore_ia": round(float(prob_detracao * 100), 2)
            }
        }

    except Exception as e:
        return {"status": "Erro", "mensagem": f"Falha na inferência técnica: {str(e)}"}

# --- SIMULAÇÃO EXECUTIVA (TESTE DE MESA) ---
if __name__ == "__main__":
    # Exemplo: Cliente com atraso acima do ponto de ruptura
    cliente_teste = {
        'customer_age': 35,
        'customer_tenure_months': 12,
        'order_value': 450.0,
        'items_quantity': 2,
        'delivery_time_days': 3,
        'delivery_delay_days': 4, # 🚨 Ultrapassou o Ponto de Ruptura (3 dias)
        'customer_service_contacts': 1,
        'customer_region_Sudeste': 1
    }
    
    res = predict_customer_satisfaction(cliente_teste)
    
    print("\n" + "═"*60)
    print("🚀 PAYFLOW AI: RELATÓRIO DE PREDIÇÃO ESTRATÉGICA")
    print("═"*60)
    
    if res["status"] == "Sucesso":
        print(f"📊 DIAGNÓSTICO: {res['diagnostico']}")
        print(f"📉 RISCO DE DETRAÇÃO: {res['probabilidade_detracao']}")
        print(f"🚛 LOGÍSTICA: {res['insight_logistico']}")
        print(f"💡 RECOMENDAÇÃO: {res['plano_de_acao']}")
    else:
        print(f"❌ ERRO: {res['mensagem']}")
    
    print("═"*60 + "\n")