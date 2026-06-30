# Online Shoppers Intention Prediction

Prediksi ini dibangun menggunakan **Streamlit** untuk melakukan prediksi manual dan simulasi prediksi secara *real-time* terhadap sesi pengunjung situs *e-commerce*.

**Fitur Utama**:
1. Prediksi Manual
2. Simulasi Prediksi Real-Time

## Tentang
Aplikasi ini melakukan prediksi terhadap data masukkan user, berupa data sesi kunjungan *e-commerce*. Fokus utama dari prediksi ini adalah menilai potensi pengunjung dalam setiap sesuai untuk melakukan pembelian.

## Dataset
Dataset yang digunakan dalam proyek ini diadaptasi dari **Online Shoppers Purchasing Intention Dataset** (tersedia di UCI Machine Learning Repository) 

## Struktur File
Berikut adalah struktur direktori pada repositori ini:

```text
online_shopper_dashboard
 ┣ data
 ┃ ┗ online_shoppers_intetion.csv
 ┣ models
 ┃ ┗ shopper_best_model.pkl
 ┣ .gitignore
 ┣ README.md
 ┣ requirements.txt
 ┗ streamlit_app.py
```

## Deployment (Localhost)
*Clone* repositori
```text
git clone [https://github.com/veenda/online-shopper-dashboard.git](https://github.com/veenda/online-shopper-dashboard.git)
cd online-shopper-dashboard
```

Buat dan aktifkan *virtual environment*
```text
python -m venv .venv
.venv\Scripts\activate
```

Install *library*
```text
pip install -r requirements.txt
```

Jalankan aplikasi Streamlit
```text
streamlit run streamlit_app.py
```
