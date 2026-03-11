import joblib
import pandas as pd
import os

# 1. Configurações de Caminho Dinâmico
# Tenta achar a pasta 'models' na pasta atual ou na pasta pai (..)
MODEL_PATH = os.path.join('models', 'modelo_risco_payflow.pkl')
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join('..', 'models', 'modelo_risco_payflow.pkl')

def carregar_modelo():
    """Carrega o modelo .pkl do disco com validação de caminho."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"❌ Erro: Modelo não encontrado em {MODEL_PATH}. Verifique se a pasta 'models' existe.")
    return joblib.load(MODEL_PATH)

def processar_entrada(dados_brutos, colunas_treino):
    """
    Transforma dados (dict ou DataFrame) para o formato do modelo.
    Garante as colunas do treino e realiza Feature Engineering.
    """
    df = pd.DataFrame(dados_brutos) if isinstance(dados_brutos, list) else pd.DataFrame([dados_brutos])
    
    # Feature Engineering (Métrica de Negócio)
    df['comprometimento_renda'] = df['valor_solicitado'] / (df['renda_mensal'] + 1)
    
    # Aplica One-Hot Encoding (Dummies)
    df_processado = pd.get_dummies(df)
    
    # Alinhamento de Colunas
    for col in colunas_treino:
        if col not in df_processado.columns:
            df_processado[col] = 0
            
    return df_processado[colunas_treino]

def analisar_csv_completo(caminho_csv):
    """Lê o CSV, faz as predições e filtra os clientes de Baixo Risco."""
    try:
        modelo = carregar_modelo()
        colunas_esperadas = modelo.feature_names_in_
        
        df_original = pd.read_csv(caminho_csv)
        print(f"📊 Base carregada: {len(df_original)} registros encontrados.")

        X_input = processar_entrada(df_original.to_dict('records'), colunas_esperadas)
        
        probs = modelo.predict_proba(X_input)[:, 1]
        
        df_original['probabilidade_risco'] = probs
        df_original['status_ia'] = ['ALTO RISCO' if p > 0.5 else 'BAIXO RISCO' for p in probs]
        
        aprovados = df_original[df_original['status_ia'] == 'BAIXO RISCO'].copy()
        return aprovados

    except Exception as e:
        print(f"❌ Erro no processamento em lote: {e}")
        return pd.DataFrame()

def analisar_cliente_unico(dados_cliente):
    """Executa a análise para apenas um cliente (simulação individual)."""
    try:
        modelo = carregar_modelo()
        X_input = processar_entrada(dados_cliente, modelo.feature_names_in_)
        prob = modelo.predict_proba(X_input)[0][1]
        
        status = "🟢 BAIXO RISCO" if prob <= 0.5 else "🔴 ALTO RISCO"
        
        print("\n" + "="*40)
        print(f"       RESULTADO INDIVIDUAL       ")
        print("="*40)
        print(f" Status: {status}")
        print(f" Risco Estimado: {prob:.2%}")
        print("="*40 + "\n")
    except Exception as e:
        print(f"❌ Erro na análise individual: {e}")

if __name__ == "__main__":
    ARQUIVO_DADOS = 'payflow_credit_risk.csv'

    if os.path.exists(ARQUIVO_DADOS):
        # MODO BATCH (PROCESSAMENTO EM MASSA)
        df_aprovados = analisar_csv_completo(ARQUIVO_DADOS)
        
        if not df_aprovados.empty:
            print(f"✅ Sucesso! {len(df_aprovados)} clientes de Baixo Risco identificados.")
            
            # Seleção dinâmica de colunas para exibição
            cols_interesse = ['nome', 'email', 'score_credito', 'probabilidade_risco']
            cols_existentes = [c for c in cols_interesse if c in df_aprovados.columns]
            
            if not cols_existentes:
                cols_existentes = df_aprovados.columns[:3].tolist() + ['probabilidade_risco']
                
            print("\n--- AMOSTRA DE CLIENTES APROVADOS ---")
            print(df_aprovados[cols_existentes].head(10))
            
            # Salva o resultado final
            df_aprovados.to_csv('clientes_baixo_risco_selecionados.csv', index=False)
            print("\n💾 Lista salva em: clientes_baixo_risco_selecionados.csv")
    else:
        print(f"⚠️ Arquivo {ARQUIVO_DADOS} não encontrado na pasta atual.")
        # Simulação individual como fallback
        cliente_teste = {'idade': 35, 'renda_mensal': 7000, 'valor_solicitado': 5000, 'score_credito': 750}
        analisar_cliente_unico(cliente_teste)