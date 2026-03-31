import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

# --- Rigor de Engenharia: Localização de Módulos ---
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from idhm import find_idh_file, load_and_clean_idh, run_data_audit

# --- Configuração da Página ---
st.set_page_config(page_title="PayFlow | IDHM Intelligence", layout="wide", page_icon="🌍")

# --- UI/UX: Estilo para garantir contraste nas métricas ---
st.markdown("""
    <style>
    /* Fundo principal */
    .main { background-color: #0e1117; } 
    
    /* Estilização dos Cards de Métrica para contraste total */
    [data-testid="stMetricValue"] {
        color: #000000 !important; 
        font-weight: bold !important;
    }
    [data-testid="stMetricLabel"] {
        color: #333333 !important;
    }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3); 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 Inteligência Territorial: Análise de Oportunidades IDHM")
st.markdown("""
Esta aplicação identifica **Territórios Premium** para entrega de bons produtos, 
utilizando a régua de corte de **IDHM ≥ 0.700** validada estrategicamente.
""")

# --- Carga de Dados ---
@st.cache_data
def get_data():
    path = find_idh_file()
    if path:
        df = load_and_clean_idh(path)
        for col in ['idhm', 'idhm_educacao', 'idhm_longevidade', 'idhm_renda']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Inserindo a lógica de Status solicitada
        df['status'] = df['idhm'].apply(lambda x: '✅ Premium' if x >= 0.7 else '⚠️ Em Desenvolvimento')
        return df
    return None

df = get_data()

if df is not None:
    # --- Sidebar: Filtros de Negócio ---
    st.sidebar.header("🎯 Filtros Estratégicos")
    
    # 1. Filtro de Status
    status_options = sorted(df['status'].unique().tolist())
    selected_status = st.sidebar.multiselect(
        "Classificação de Mercado:", 
        status_options, 
        default=[opt for opt in status_options if 'Premium' in opt]
    )
    
    # 2. Filtro de Estados (Dinâmico para evitar erros de Case Sensitive)
    ufs_disponiveis = sorted(df['nome_da_unidade_da_federacao'].unique().tolist())
    
    # Lista de desejados
    desejados = ['SÃO PAULO', 'SANTA CATARINA', 'DISTRITO FEDERAL', 'PARANÁ', 'RIO GRANDE DO SUL']
    default_ufs = [uf for uf in ufs_disponiveis if uf in desejados]
    
    if not default_ufs:
        default_ufs = ufs_disponiveis[:5]

    selected_uf = st.sidebar.multiselect(
        "Selecione os Estados:", 
        ufs_disponiveis, 
        default=default_ufs
    )
    
    # 3. Slider de IDH
    idh_min = st.sidebar.slider(
        "Piso de IDH Municipal (Meta: 0.7):", 
        float(df['idhm'].min()), 
        float(df['idhm'].max()), 
        0.70
    )

    # --- Filtragem ---
    df_filtered = df[
        (df['nome_da_unidade_da_federacao'].isin(selected_uf)) & 
        (df['idhm'] >= idh_min) &
        (df['status'].isin(selected_status))
    ]

    # --- Métricas de Resumo ---
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Cidades Selecionadas", len(df_filtered))
    c2.metric("IDHM Médio da Amostra", round(df_filtered['idhm'].mean(), 3) if not df_filtered.empty else 0)
    c3.metric("Ticket Médio (Proxy Renda)", round(df_filtered['idhm_renda'].mean(), 3) if not df_filtered.empty else 0)
    c4.metric("Nível de Educação", round(df_filtered['idhm_educacao'].mean(), 3) if not df_filtered.empty else 0)

    st.divider()

    if not df_filtered.empty:
        # --- Linha 1 de Gráficos ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🏆 Ranking de Cidades por Potencial de Renda")
            fig_bar = px.bar(
                df_filtered.sort_values(by='idhm_renda', ascending=False).head(15), 
                x='idhm_renda', y='municipio', color='idhm_renda',
                orientation='h',
                color_continuous_scale='Magma',
                labels={'idhm_renda': 'IDH Renda', 'municipio': 'Cidade'}
            )
            fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            st.subheader("📈 Matriz de Decisão: Renda vs Educação")
            fig_scatter = px.scatter(
                df_filtered, x='idhm_educacao', y='idhm_renda', 
                size='idhm', color='status',
                hover_name='municipio',
                color_discrete_map={'✅ Premium': '#2E7D32', '⚠️ Em Desenvolvimento': '#9E9E9E'},
                labels={'idhm_educacao': 'IDH Educação', 'idhm_renda': 'IDH Renda'}
            )
            fig_scatter.add_hline(y=0.7, line_dash="dash", line_color="red", annotation_text="Meta 0.7")
            st.plotly_chart(fig_scatter, use_container_width=True)

        # --- Conclusão Automática ---
        st.info(f"**Insight de Negócio:** Atualmente você está visualizando {len(df_filtered)} cidades que atendem aos critérios de filtro. O foco deve priorizar as cidades com maior IDH Renda para otimização de conversão.")
    else:
        st.warning("Nenhum dado encontrado para os filtros selecionados. Ajuste os critérios na barra lateral.")

    # --- Auditoria e Dados ---
    with st.expander("🛠️ Auditoria de Dados Brutos"):
        st.dataframe(df_filtered, use_container_width=True)

else:
    st.error("Erro Crítico: Base de dados não carregada. Verifique os caminhos no arquivo idhm.py.")