import pytest
import os
import joblib
import pandas as pd
# Mudamos de 'from src.predict' para 'from predict' 
# porque o arquivo está na raiz, não dentro de src!
from predict import carregar_modelo, processar_entrada

# Teste 1: Verificar se o arquivo do modelo existe e carrega
def test_modelo_carregado():
    MODEL_PATH = 'models/modelo_risco_payflow.pkl'
    assert os.path.exists(MODEL_PATH), "O arquivo .pkl não foi encontrado!"
    modelo = carregar_modelo()
    assert modelo is not None, "Falha ao carregar o modelo joblib"

# Teste 2: Verificar se o processamento gera o número correto de colunas
def test_processamento_colunas():
    modelo = carregar_modelo()
    colunas_esperadas = modelo.feature_names_in_ # Espera-se 25 colunas
    
    cliente_fake = {
        'idade': 30,
        'renda_mensal': 5000,
        'valor_solicitado': 10000,
        'score_credito': 600,
        'tempo_emprego_anos': 3
    }
    
    df_result = processar_entrada(cliente_fake, colunas_esperadas)
    assert df_result.shape[1] == len(colunas_esperadas), f"O processamento deveria retornar {len(colunas_esperadas)} colunas"