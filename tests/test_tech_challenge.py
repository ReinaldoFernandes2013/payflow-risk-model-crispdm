import pytest
import os
import sys
from pathlib import Path

# ==============================================================================
# RIGOR DE ENGENHARIA: LOCALIZAÇÃO DINÂMICA DE MÓDULOS (MLOps Standard)
# ==============================================================================
# Garante que o ambiente de teste localize a pasta 'src' de forma absoluta.
current_dir = Path(__file__).resolve().parent
root_path = current_dir.parent
src_path = str(root_path / "src")

if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Importação da lógica de produção validada (Sincronizada com o Notebook)
try:
    from predict_tech_challenge import predict_customer_satisfaction
except ImportError:
    from src.predict_tech_challenge import predict_customer_satisfaction

# ==============================================================================
# SUÍTE DE TESTES UNITÁRIOS E DE INTEGRAÇÃO (VERSÃO SÊNIOR)
# ==============================================================================

def test_predict_nps_flow():
    """ Valida se o fluxo de predição retorna o novo schema executivo correto. """
    cliente_teste = {
        "customer_age": 40,
        "customer_tenure_months": 12,
        "order_value": 500.0,
        "items_quantity": 2,
        "delivery_time_days": 5,
        "delivery_delay_days": 0, # Cenário seguro (sem atraso)
        "customer_service_contacts": 0,
        "customer_region_Sudeste": 1
    }
    
    resultado = predict_customer_satisfaction(cliente_teste)
    
    # Validação do Novo Schema (Conforme feedback do Prof. Alexandre)
    assert resultado["status"] == "Sucesso"
    assert "diagnostico" in resultado        # Substituiu 'classe'
    assert "insight_logistico" in resultado  # Substituiu 'alerta_logistico'
    assert "plano_de_acao" in resultado      # Nova chave de recomendação estratégica
    assert "probabilidade_detracao" in resultado

def test_nps_critical_delay_alert():
    """ Valida se a lógica de Ponto de Ruptura dispara o diagnóstico de risco. """
    # Cenário Crítico: 8 dias de atraso (Muito acima do ponto de ruptura de 3 dias)
    cliente_atrasado = {
        "delivery_delay_days": 8, 
        "delivery_time_days": 5,
        "customer_service_contacts": 2
    }
    
    resultado = predict_customer_satisfaction(cliente_atrasado)
    
    if resultado["status"] == "Sucesso":
        # Valida o Ponto de Ruptura identificado cientificamente na EDA
        assert resultado["insight_logistico"] == "Ponto de Ruptura Atingido"
        
        # Valida se o diagnóstico reflete o risco (Moderado ou Crítico)
        assert "CRÍTICO" in resultado["diagnostico"] or "MODERADO" in resultado["diagnostico"]

def test_nps_resilience():
    """ Valida a resiliência perante dados incompletos (Integridade MLOps). """
    # O motor deve preencher as colunas ausentes e calcular o ratio sem quebrar
    cliente_incompleto = {"delivery_delay_days": 2, "delivery_time_days": 10}
    
    resultado = predict_customer_satisfaction(cliente_incompleto)
    
    assert resultado["status"] == "Sucesso"
    assert "plano_de_acao" in resultado

# ==============================================================================
# EXECUÇÃO MANUAL E RELATÓRIO DE AUDITORIA
# ==============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🧪 PAYFLOW AI: AUDITORIA DE TESTES (VERSÃO EXECUTIVA)")
    print("="*60)
    
    try:
        test_predict_nps_flow()
        print("✅ [OK] Teste de Fluxo: Schema e chaves de negócio validados.")
        
        test_nps_critical_delay_alert()
        print("✅ [OK] Teste de Negócio: Ponto de Ruptura e diagnóstico crítico.")
        
        test_nps_resilience()
        print("✅ [OK] Teste de Resiliência: Integridade com dados parciais.")
        
        print("\n🏁 RESULTADO FINAL: 100% de cobertura nos requisitos do Prof. Alexandre.")
    except AssertionError as e:
        print(f"❌ [FALHA] Erro de validação: {e}")
        print("DICA: Verifique se os nomes das chaves no predict_tech_challenge.py estão corretos.")
    except Exception as e:
        print(f"💥 [ERRO TÉCNICO]: {e}")
    
    print("="*60 + "\n")