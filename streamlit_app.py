import streamlit as st
import pandas as pd
import numpy as np
import time
import joblib

# HALAMAN STREAMLIT
st.set_page_config(
    page_title="Prediksi Niat Pembeli",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"], .stApp, p, span, div, h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: #1E1E1E !important;
    }
    .stApp, .stApp > header { background-color: #F0F2F6 !important; }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 16px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important; 
        padding: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: #FFFFFF !important;
    }

    div[data-testid="stFormSubmitButton"] button {
        background-color: #1976D2 !important;
        color: white !important;
        border: none !important;
        width: 100%;
        font-weight: 600;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        color: #1976D2 !important;
        font-weight: 700 !important;
    }
    
    /* Modifikasi Tabs */
    button[data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Prediksi Niat Pembeli")

# DATASET
@st.cache_resource
def load_model():
    return joblib.load('models/shopper_best_model.pkl')

@st.cache_data
def load_data():
    return pd.read_csv('data/online_shoppers_intention.csv')

model = load_model()
df_stream = load_data()

# TABS
tab1, tab2 = st.tabs(["Prediksi Manual", "Simulasi Prediksi Real-Time"])

# TAB 1: PREDIKSI MANUAL
with tab1:
    col_input, col_result = st.columns([7, 3], gap="medium")

    with col_input:
        with st.form("prediction_form", border=True):
            st.subheader("Input Data")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                admin = st.number_input("Halaman Admin", min_value=0, value=0, step=1)
                admin_dur = st.number_input("Durasi Admin (s)", min_value=0.0, value=0.0, step=10.0)
                bounce = st.number_input("Bounce Rates", min_value=0.0, max_value=0.2, value=0.0, format="%.3f")
                visitor = st.selectbox("Tipe Pengunjung", ["Returning_Visitor", "New_Visitor", "Other"])
            with c2:
                info = st.number_input("Halaman Info", min_value=0, value=0, step=1)
                info_dur = st.number_input("Durasi Info (s)", min_value=0.0, value=0.0, step=10.0)
                exit_rate = st.number_input("Exit Rates", min_value=0.0, max_value=0.2, value=0.02, format="%.3f")
                month = st.selectbox("Bulan", ["Feb", "Mar", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], index=8)
            with c3:
                prod = st.number_input("Halaman Produk", min_value=0, value=10, step=1)
                prod_dur = st.number_input("Durasi Produk (s)", min_value=0.0, value=150.0, step=10.0)
                page_val = st.number_input("Page Values", min_value=0.0, value=15.5, step=1.0)
                special = st.slider("Special Day", 0.0, 1.0, 0.0, step=0.2)
            
            c4, c5, c6, c7 = st.columns(4)
            with c4:
                os = st.selectbox("OS", [1, 2, 3, 4, 5, 6, 7, 8], index=1)
            with c5:
                browser = st.selectbox("Browser", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], index=1)
            with c6:
                region = st.selectbox("Region", [1, 2, 3, 4, 5, 6, 7, 8, 9], index=0)
            with c7:
                traffic = st.selectbox("Traffic", list(range(1, 21)), index=1)
            
            weekend = st.checkbox("Akhir Pekan", value=False)
            
            submitted = st.form_submit_button("Analisis")

    with col_result:
        with st.container(border=True):
            st.subheader("Hasil")
            
            if submitted:
                prod_dur_per_page = prod_dur / (prod + 1e-5)
                total_pages = admin + info + prod
                total_duration = admin_dur + info_dur + prod_dur
                prod_dur_log = np.log1p(prod_dur)
                weekend_int = 1 if weekend else 0
                
                input_data = pd.DataFrame([{
                    'Administrative': admin,
                    'Administrative_Duration': admin_dur,
                    'Informational': info,
                    'Informational_Duration': info_dur,
                    'ProductRelated': prod,
                    'ProductRelated_Duration': prod_dur_log,
                    'BounceRates': bounce,
                    'ExitRates': exit_rate,
                    'PageValues': page_val,
                    'SpecialDay': special,
                    'ProductRelated_Duration_Per_Page': prod_dur_per_page,
                    'Total_Pages_Visited': total_pages,
                    'Total_Duration_Spent': total_duration,
                    'Month': month,
                    'OperatingSystems': os,
                    'Browser': browser,
                    'Region': region,
                    'TrafficType': traffic,
                    'VisitorType': visitor,
                    'Weekend': weekend_int
                }])
                
                prediction = model.predict(input_data)[0]
                probability = model.predict_proba(input_data)[0][1]
                
                st.metric(label="Probabilitas", value=f"{probability * 100:.1f}%")
                
                if prediction == 1:
                    st.success("Potensi: Tinggi")
                else:
                    st.info("Potensi: Rendah")
            else:
                st.write("Menunggu input.")

# TAB 2: SIMULASI PREDIKSI REAL-TIME
with tab2:
    if 'is_running' not in st.session_state:
        st.session_state.is_running = False

    col_btn1, col_btn2, _ = st.columns([2, 2, 8])
    with col_btn1:
        if st.button("Mulai", use_container_width=True):
            st.session_state.is_running = True
    with col_btn2:
        if st.button("Berhenti", use_container_width=True):
            st.session_state.is_running = False

    st.write("")

    col1, col2, col3 = st.columns(3, gap="medium")
    bento_total = col1.empty()
    bento_buyers = col2.empty()
    bento_rate = col3.empty()

    col_left, col_right = st.columns([1, 2], gap="medium")
    with col_left:
        bento_current = st.empty()
    with col_right:
        bento_leads = st.empty()

    if st.session_state.is_running:
        total_visitors = 0
        potential_buyers = 0
        hot_leads_data = []

        for index, row in df_stream.iterrows():
            if not st.session_state.is_running:
                break
                
            X_live = pd.DataFrame([row.drop('Revenue')]) 

            # Rekayasa fitur
            X_live['Total_Pages_Visited'] = X_live['Administrative'] + X_live['Informational'] + X_live['ProductRelated']
            X_live['Total_Duration_Spent'] = X_live['Administrative_Duration'] + X_live['Informational_Duration'] + X_live['ProductRelated_Duration']
            X_live['ProductRelated_Duration_Per_Page'] = X_live['ProductRelated_Duration'] / (X_live['ProductRelated'] + 1e-5)
            X_live['ProductRelated_Duration'] = np.log1p(X_live['ProductRelated_Duration'])
            X_live['Weekend'] = X_live['Weekend'].astype(int)
            
            prediction = model.predict(X_live)[0]
            probability = model.predict_proba(X_live)[0][1]

            total_visitors += 1
            if prediction == 1:
                potential_buyers += 1
                hot_leads_data.insert(0, {
                    "ID": total_visitors,
                    "Probabilitas": f"{probability*100:.1f}%",
                    "Page Values": f"{row['PageValues']:.2f}",
                    "Tipe": row['VisitorType']
                })
            
            conversion_rate = (potential_buyers / total_visitors) * 100 if total_visitors > 0 else 0

            with bento_total.container(border=True):
                st.metric(label="Total Sesi", value=total_visitors)
            with bento_buyers.container(border=True):
                st.metric(label="Prospek", value=potential_buyers)
            with bento_rate.container(border=True):
                st.metric(label="Konversi", value=f"{conversion_rate:.1f}%")

            with bento_current.container(border=True):
                st.subheader(f"Sesi #{total_visitors}")
                st.write(f"Page Values: {row['PageValues']}")
                if prediction == 1:
                    st.success("Potensi: Tinggi")
                else:
                    st.info("Potensi: Rendah")

            with bento_leads.container(border=True):
                st.subheader("Daftar Prospek")
                if hot_leads_data:
                    st.dataframe(pd.DataFrame(hot_leads_data[:5]), use_container_width=True, hide_index=True)
                else:
                    st.write("N/A")

            time.sleep(1)