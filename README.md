# Online Shoppers Interaction Dashboard

Sebuah dasbor analitik interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis perilaku pengunjung situs *e-commerce*. Dasbor ini dirancang dengan antarmuka **Bento UI** yang modern, bersih, dan responsif guna membantu tim bisnis memahami metrik kunci, tren konversi, serta faktor pendorong utama yang membuat pengunjung memutuskan untuk berbelanja.

## Tentang
Aplikasi ini melakukan visualisasi data historis dari sesi kunjungan *e-commerce*. Fokus utama dari dasbor ini adalah membedah metrik kualitas sesi (seperti *PageValues*) dan hubungannya dengan probabilitas transaksi (konversi).

Fitur Utama:
- **KPI Metrics:** Pemantauan instan untuk Total Kunjungan, Total Konversi, dan *Conversion Rate*.
- **Trend Analysis:** Distribusi volume transaksi berdasarkan bulan kalender.
- **Behavioral Insights:** Analisis kepadatan kualitas halaman (*PageValues*) antara pengunjung yang membeli vs tidak membeli.
- **Audience Segmentation:** Perbandingan rasio konversi berdasarkan tipe pengunjung (*Returning* vs *New Visitor*).

## Dataset
Dataset yang digunakan dalam proyek ini diadaptasi dari **Online Shoppers Purchasing Intention Dataset** (tersedia di UCI Machine Learning Repository) 

Data ini merekam metrik aktivitas penjelajahan *real-time* (Google Analytics) seperti durasi kunjungan di berbagai tipe halaman (Admin, Info, Produk), metrik pentalan (*Bounce/Exit Rates*), hingga label akhir apakah pengunjung tersebut melakukan transaksi (`Revenue` = `True/False`). 

## Struktur File
Berikut adalah hierarki direktori pada repositori ini:

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
