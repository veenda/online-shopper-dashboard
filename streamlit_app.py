import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# KONFIGURASI HALAMAN STREAMLIT
st.set_page_config(
    page_title="Online Shoppers Interaction Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Font Global & Warna Teks Gelap */
    html, body, [class*="css"], .stApp, p, span, div, h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: #1E1E1E !important;
    }
    
    /* Background Utama Terang (Abu-abu sangat muda) */
    .stApp, .stApp > header { 
        background-color: #F8F9FA !important; 
    }
    
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mengurangi jarak padding agar kanvas lebih rapat */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        gap: 0.5rem !important;
    }
    
    /* Desain Bento Box (Putih Murni dengan Shadow Lembut) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1px solid #EAEAEA !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
        padding: 0.2rem !important;
    }
    
    /* Memastikan lapisan dalam bento juga putih */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
    }

    /* Modifikasi text metrik KPI */
    div[data-testid="stMetricValue"], 
    div[data-testid="stMetricValue"] div {
        font-size: 1.8rem !important;
        color: #1976D2 !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stMetricLabel"], 
    div[data-testid="stMetricLabel"] p {
        font-weight: 500 !important;
        color: #666666 !important;
    }
    
    /* Menghilangkan margin bawaan judul agar lebih rapat */
    h1 {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-bottom: 0rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# DATA LOADING
@st.cache_data
def load_data():
    return pd.read_csv('data/shoppers_stream_source.csv')

df = load_data()

# Metrik KPI
total_sessions = len(df)
total_buyers = df[df['Revenue'] == 1].shape[0]
conversion_rate = (total_buyers / total_sessions) * 100 if total_sessions > 0 else 0
avg_page_value_buyer = df[df['Revenue'] == 1]['PageValues'].mean() if total_buyers > 0 else 0

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Poppins', 'Arial']
plt.rcParams['text.color'] = '#1E1E1E'
plt.rcParams['axes.labelcolor'] = '#1E1E1E'
plt.rcParams['xtick.color'] = '#1E1E1E'
plt.rcParams['ytick.color'] = '#1E1E1E'

# LAYOUTBENTO
# Judul
with st.container(border=True):
    st.title("E-Commerce Shopper Insights")

# Baris 1: Metrik KPI
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1.container(border=True):
    st.metric("Total Sesi Kunjungan", f"{total_sessions:,}")
with col2.container(border=True):
    st.metric("Total Konversi (Beli)", f"{total_buyers:,}")
with col3.container(border=True):
    st.metric("Conversion Rate", f"{conversion_rate:.1f}%")
with col4.container(border=True):
    st.metric("Rata-rata PageValues (Pembeli)", f"{avg_page_value_buyer:.1f}")

# Baris 2: Visualisasi Data
col5, col6, col7 = st.columns(3, gap="small")

with col5.container(border=True):
    st.subheader("Bulan Paling Ramai Transaksi")
    
    monthly_data = df[df['Revenue'] == 1]['Month'].value_counts().reset_index()
    monthly_data.columns = ['Bulan', 'Jumlah Transaksi']
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    sns.barplot(data=monthly_data, x='Bulan', y='Jumlah Transaksi', palette='Blues_r', ax=ax)
    ax.set_ylabel('')
    ax.set_xlabel('')
    st.pyplot(fig)

with col6.container(border=True):
    st.subheader("Dampak Kualitas Halaman")
    
    fig2, ax2 = plt.subplots(figsize=(6, 3.5))
    fig2.patch.set_alpha(0.0)
    ax2.patch.set_alpha(0.0)
    
    sns.kdeplot(data=df, x='PageValues', hue='Revenue', fill=True, common_norm=False, palette={0: 'gray', 1: '#1976D2'}, ax=ax2)
    ax2.set_xlim(-5, 100)
    ax2.set_ylabel('Kepadatan')
    ax2.legend(['Beli (1)', 'Tidak Beli (0)'])
    st.pyplot(fig2)

with col7.container(border=True):
    st.subheader("Konversi Tipe Pengunjung")
    
    filtered_df = df[df['VisitorType'] != 'Other']
    
    visitor_data = filtered_df.groupby('VisitorType')['Revenue'].mean().reset_index()
    visitor_data['Revenue'] = visitor_data['Revenue'] * 100
    
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    fig3.patch.set_alpha(0.0)
    ax3.patch.set_alpha(0.0)
    
    sns.barplot(data=visitor_data, y='VisitorType', x='Revenue', palette='viridis', ax=ax3)
    ax3.set_xlabel('Conversion Rate (%)')
    ax3.set_ylabel('')
    st.pyplot(fig3)