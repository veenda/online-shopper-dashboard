# Online Shoppers Interaction Dashboard

Dasbor analitik interaktif ini dibangun menggunakan **Streamlit** untuk menganalisis perilaku pengunjung situs *e-commerce*.

## Tentang
Aplikasi ini melakukan visualisasi data historis dari sesi kunjungan *e-commerce*. Fokus utama dari dasbor ini adalah membedah metrik kualitas sesi (seperti *PageValues*) dan hubungannya dengan probabilitas transaksi (konversi).

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
