# 📊 Customer Churn Prediction

### Nama : Wahyu Dwi Wicaksono

### NIM : A11.2023.15261

---

## 📖 Deskripsi Proyek

Proyek ini merupakan implementasi Machine Learning untuk memprediksi apakah seorang pelanggan berpotensi melakukan **Churn** (berhenti menggunakan layanan) atau **Tidak Churn** berdasarkan data perilaku, aktivitas, dan transaksi pelanggan.

Proyek dikembangkan sebagai tugas **UAS Bengkel Koding Data Science** dengan menerapkan tahapan Data Science mulai dari Data Understanding, Exploratory Data Analysis (EDA), Data Preprocessing, Modeling, Evaluasi Model, hingga Deployment menggunakan Streamlit.

---

## 🎯 Tujuan Proyek

* Menganalisis faktor-faktor yang memengaruhi churn pelanggan.
* Membangun model machine learning untuk memprediksi churn pelanggan.
* Membandingkan performa beberapa algoritma machine learning.
* Mengevaluasi model menggunakan berbagai metrik klasifikasi.
* Mengembangkan aplikasi Streamlit untuk prediksi churn secara interaktif.

---

## 📂 Dataset

Dataset yang digunakan berisi informasi pelanggan, aktivitas penggunaan layanan, serta data transaksi pelanggan.

### Fitur Dataset

* Gender
* Age
* Country
* City
* Signup Date
* Last Purchase Date
* Acquisition Channel
* Device Type
* Subscription Type
* Is Premium User
* Total Visits
* Average Session Time
* Pages Per Session
* Email Open Rate
* Email Click Rate
* Total Spent
* Average Order Value
* Discount Used
* Support Tickets
* Refund Requested
* Delivery Delay Days
* Payment Method
* Satisfaction Score
* NPS Score
* Marketing Spend Per User
* Lifetime Value
* Last 3 Month Purchase Frequency

### Target

```text
churn
```

Keterangan:

* 0 = Tidak Churn
* 1 = Churn

Jumlah Data:

```text
15.000 Data Pelanggan
```

---

## 🔍 Data Understanding

Tahapan yang dilakukan:

* Memahami struktur dataset
* Mengecek tipe data
* Mengecek missing values
* Mengecek duplicate data
* Menentukan fitur dan target

---

## 🛠 Data Preprocessing

### 1. Handling Missing Values

* Mengidentifikasi nilai kosong pada dataset
* Menghapus atau menangani data yang memiliki missing value

### 2. Handling Duplicate Data

* Mengecek data duplikat
* Menghapus data duplikat jika ditemukan

### 3. Label Encoding

Mengubah seluruh fitur kategorikal menjadi numerik menggunakan LabelEncoder agar dapat diproses oleh algoritma machine learning.

### 4. Train Test Split

Membagi dataset menjadi:

* Data Training (80%)
* Data Testing (20%)

---

## 📊 Exploratory Data Analysis (EDA)

Analisis yang dilakukan meliputi:

### Distribusi Data

* Age
* Total Visits
* Total Spent
* Average Session Time
* Lifetime Value
* Dan fitur numerik lainnya

### Churn Distribution

Analisis distribusi pelanggan yang churn dan tidak churn.

### Correlation Heatmap

Analisis hubungan antar fitur.

### Boxplot Analysis

Analisis outlier pada fitur numerik.

### Relationship Analysis

Analisis hubungan antara fitur dengan target churn.

---

## 🤖 Modeling

Penelitian menggunakan 3 algoritma machine learning:

### 1. Logistic Regression

Model klasifikasi linear untuk prediksi churn.

### 2. Random Forest

Model ensemble berbasis decision tree.

### 3. Voting Classifier

Model ensemble yang menggabungkan beberapa algoritma.

---

## 🧪 Skenario Eksperimen

### 1. Direct Modeling

Model dilatih langsung menggunakan data hasil preprocessing dasar.

### 2. Modeling dengan Preprocessing

Model dilatih setelah dilakukan preprocessing tambahan.

### 3. Hyperparameter Tuning

Optimasi parameter model untuk memperoleh performa terbaik.

---

## 📈 Total Model yang Dihasilkan

```text
3 Algoritma × 3 Skenario = 9 Model
```

### Direct Modeling

1. Logistic Regression
2. Random Forest
3. Voting Classifier

### Preprocessing

4. Logistic Regression
5. Random Forest
6. Voting Classifier

### Hyperparameter Tuning

7. Logistic Regression
8. Random Forest
9. Voting Classifier

---

## 📏 Evaluasi Model

Model dievaluasi menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## 🏆 Model Terbaik

```text
Random Forest (Preprocessing)
```

### Alasan Pemilihan

* Mampu mendeteksi pelanggan churn lebih baik dibanding model lainnya.
* Memiliki performa yang lebih seimbang berdasarkan Confusion Matrix.
* Menghasilkan nilai Recall dan F1-Score yang lebih baik untuk kasus churn prediction.

---

## 📌 Feature Importance

Fitur yang paling berpengaruh terhadap churn:

1. Total Spent
2. Satisfaction Score
3. Support Tickets
4. Average Session Time
5. Lifetime Value
6. Pages Per Session
7. Average Order Value

---

## 🚀 Deployment

Model terbaik disimpan menggunakan Joblib:

```python
joblib.dump(best_model, "best_model.pkl")
```

Aplikasi deployment dibangun menggunakan:

* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

## 🌐 Live Demo

Aplikasi Customer Churn Prediction telah dideploy menggunakan Streamlit.

### Link Aplikasi

```text
https://YOUR-STREAMLIT-URL.streamlit.app/
```

### Fitur Aplikasi

* Input data pelanggan secara interaktif.
* Prediksi churn secara real-time.
* Menggunakan model machine learning terbaik.
* Tampilan sederhana dan mudah digunakan.

### Cara Menggunakan

1. Buka aplikasi melalui browser.
2. Masukkan data pelanggan.
3. Klik tombol **Prediksi Churn**.
4. Sistem akan menampilkan hasil prediksi.

### Output

* **0 = Tidak Churn**
* **1 = Churn**

---

## 📁 Struktur Project

```text
bengkelkodinguas/
│
├── data/
│   └── customer_churn.csv
│
├── notebook/
│   └── bengkelkodinguas.ipynb
│
├── deployment/
│   ├── app.py
│   └── best_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Instalasi

Clone repository:

```bash
git clone https://github.com/wahyudwiw/uas_Bengkel_koding.git
cd uas_Bengkel_koding
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

```bash
streamlit run deployment/app.py
```

atau

```bash
python -m streamlit run deployment/app.py
```

---

## 📓 Google Colab

Notebook dapat diakses melalui:

```text
https://colab.research.google.com/drive/1cUQDeBWlQZoAGzO6OvNh0U-lLmN6I5-d?usp=sharing
```

---

## 🔗 Repository GitHub

```text
https://github.com/wahyudwiw/uas_Bengkel_koding
```

---

## 💻 Tools & Library

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

## 👨‍🎓 Author

**Wahyu Dwi Wicaksono**

**NIM : A11.2023.15261**

Teknik Informatika

Universitas Dian Nuswantoro (UDINUS)

---

## 📄 License

Project ini dibuat untuk keperluan pembelajaran dan penyelesaian tugas UAS Bengkel Koding Data Science.

