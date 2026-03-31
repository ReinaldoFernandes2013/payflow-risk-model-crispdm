import pytest
import sys
import os
import pandas as pd
from pathlib import Path

# --- Rigor de Engenharia: Localização Dinâmica de Módulos ---
current_file = Path(__file__).resolve()
root_path = current_file.parent.parent
src_path = str(root_path / "src")

if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Tentativa de importação absoluta do motor IDH
try:
    from idhm import find_idh_file, load_and_clean_idh, run_data_audit
except ImportError as e:
    print(f"\n❌ Erro de Importação: O motor 'idhm.py' não foi localizado em {src_path}")
    raise e

def test_file_discovery():
    """Valida se o motor de busca localiza a planilha IDH_2010.xls."""
    path = find_idh_file()
    assert path is not None, "❌ Erro: O motor de busca não localizou a planilha."
    assert path.exists(), "❌ Erro: O arquivo físico não existe no disco."

def test_data_cleaning_and_status_logic():
    """Valida o Schema (incluindo a nova coluna status) e a regra de negócio de 0.7."""
    path = find_idh_file()
    df = load_and_clean_idh(path)
    
    # Lista atualizada de colunas (Agora com 7 colunas devido ao 'status')
    expected_cols = [
        'nome_da_unidade_da_federacao', 
        'municipio', 
        'idhm', 
        'idhm_educacao', 
        'idhm_longevidade', 
        'idhm_renda',
        'status' # Nova coluna adicionada
    ]
    
    # 1. Validação de Schema
    assert list(df.columns) == expected_cols, "❌ Erro: O Schema mudou ou a coluna 'status' não foi gerada."
    
    # 2. Validação da Regra de Negócio (O ponto principal do feedback do professor)
    municipio_premium = df[df['idhm'] >= 0.7].iloc[0]
    municipio_desenvolvimento = df[df['idhm'] < 0.7].iloc[0]
    
    assert municipio_premium['status'] == '✅ Premium', "❌ Erro: Falha na classificação de IDH Alto (>= 0.7)."
    assert municipio_desenvolvimento['status'] == '⚠️ Em Desenvolvimento', "❌ Erro: Falha na classificação de IDH Baixo (< 0.7)."

def test_audit_integrity():
    """Valida se a função de auditoria aprova a base carregada."""
    path = find_idh_file()
    df = load_and_clean_idh(path)
    
    # Auditoria de escala técnica (0 a 1)
    assert run_data_audit(df) is True, "❌ Erro: A base de dados falhou na auditoria técnica."

def test_numeric_consistency():
    """Garante que todos os indicadores são do tipo float (essencial para cálculos)."""
    path = find_idh_file()
    df = load_and_clean_idh(path)
    cols_numericas = ['idhm', 'idhm_educacao', 'idhm_longevidade', 'idhm_renda']
    
    for col in cols_numericas:
        assert pd.api.types.is_float_dtype(df[col]), f"❌ Erro: A coluna {col} deveria ser float."