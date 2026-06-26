# 📊 Customer Churn Prediction

## Wahyu Dwi Wicaksono

**NIM:** A11.2023.15261

---

# 📖 Deskripsi Proyek

Customer Churn Prediction merupakan aplikasi Machine Learning yang digunakan untuk memprediksi apakah seorang pelanggan berpotensi melakukan **Churn** (berhenti menggunakan layanan) atau **Loyal** berdasarkan data demografi, aktivitas penggunaan, transaksi, dan tingkat kepuasan pelanggan.

Proyek ini dikembangkan sebagai tugas **UAS Bengkel Koding Data Science** dengan menerapkan tahapan Data Science secara lengkap mulai dari Data Understanding, Exploratory Data Analysis (EDA), Data Preprocessing, Machine Learning Modeling, Hyperparameter Tuning, Evaluasi Model, hingga Deployment menggunakan Streamlit.

---

# 🎯 Tujuan Proyek

* Menganalisis faktor-faktor yang memengaruhi churn pelanggan.
* Membangun model Machine Learning untuk prediksi churn.
* Membandingkan performa beberapa algoritma klasifikasi.
* Mengevaluasi model menggunakan berbagai metrik evaluasi.
* Mengembangkan aplikasi prediksi berbasis web menggunakan Streamlit.

---

# 📂 Dataset

Dataset berisi **15.000 data pelanggan** dengan target:

**Target**

```text
churn

0 = Loyal
1 = Churn
```

## Fitur

1. Gender
2. Age
3. Country
4. City
5. Signup Date
6. Last Purchase Date
7. Acquisition Channel
8. Device Type
9. Subscription Type
10. Is Premium User
11. Total Visits
12. Average Session Time
13. Pages Per Session
14. Email Open Rate
15. Email Click Rate
16. Total Spent
17. Average Order Value
18. Discount Used
19. Coupon Code
20. Support Tickets
21. Refund Requested
22. Delivery Delay Days
23. Payment Method
24. Satisfaction Score
25. NPS Score
26. Marketing Spend Per User
27. Lifetime Value
28. Last 3 Month Purchase Frequency

---

# 🔍 Data Understanding

Tahapan yang dilakukan:

* Pemeriksaan struktur dataset
* Pemeriksaan tipe data
* Missing Value Checking
* Duplicate Checking
* Pemisahan Feature dan Target

---

# 📊 Exploratory Data Analysis (EDA)

EDA yang dilakukan meliputi:

* Distribusi Data Numerik
* Distribusi Target Churn
* Correlation Heatmap
* Boxplot Outlier
* Hubungan Feature terhadap Target

---

# 🛠 Data Preprocessing

Tahapan preprocessing meliputi:

* Handling Missing Value
* Handling Duplicate Data
* Label Encoding
* Train Test Split
* StandardScaler
* SMOTE (Synthetic Minority Oversampling Technique)

---

# 🤖 Machine Learning Modeling

Penelitian menggunakan tiga algoritma Machine Learning:

* Logistic Regression
* Random Forest
* Voting Classifier

---

# 🧪 Skenario Eksperimen

## 1. Direct Modeling

Training model menggunakan preprocessing dasar.

## 2. Modeling with Preprocessing

Training model setelah dilakukan preprocessing lanjutan.

## 3. Hyperparameter Tuning

Optimasi parameter model menggunakan Grid Search.

Total model yang dihasilkan:

```text
3 Algoritma × 3 Skenario = 9 Model
```

---

# 📈 Evaluasi Model

Evaluasi menggunakan:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

---

# 🏆 Model Terbaik

## Voting Classifier (Hyperparameter Tuning)

Performa model:

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 83.83% |
| Precision | 43.57% |
| Recall    | 74.73% |
| F1 Score  | 55.05% |

Voting Classifier dipilih sebagai model terbaik karena memberikan keseimbangan terbaik dalam mendeteksi pelanggan churn dengan nilai Recall dan F1 Score yang lebih baik dibanding model lainnya.

---

# ⭐ Feature Importance

Feature yang paling berpengaruh terhadap prediksi churn antara lain:

* Total Spent
* Satisfaction Score
* Support Tickets
* Average Session Time
* Lifetime Value
* Average Order Value
* Total Visits
* NPS Score

---

# 🚀 Deployment

Model disimpan menggunakan Joblib.

```python
joblib.dump(best_voting, "best_model.pkl")
joblib.dump(scaler, "scaler.pkl")
```

Deployment dibangun menggunakan:

* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

# 🌐 Live Demo

https://uasbengkelkoding.streamlit.app/

---

# 💻 Fitur Aplikasi

* Input data pelanggan secara interaktif
* Prediksi churn secara real-time
* Probability Meter
* Risk Classification
* Recommendation System
* Input Summary

---

# 📁 Struktur Project

```text
uas_Bengkel_koding/

│
├── deployment/
│   ├── app.py
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── bengkelkodinguas.ipynb
│
├── data/
│   └── customer_churn.csv
│
├── requirements.txt
├── README.md
```

---

# ⚙️ Instalasi

```bash
git clone https://github.com/wahyudwiw/uas_Bengkel_koding.git

cd uas_Bengkel_koding

pip install -r requirements.txt
```

---

# ▶️ Menjalankan Aplikasi

```bash
streamlit run deployment/app.py
```

atau

```bash
python -m streamlit run deployment/app.py
```

---

## 🌐 Live Demo Aplikasi Customer Churn Prediction telah dideploy menggunakan Streamlit. 

### Link Aplikasi
text
https://uasbengkelkoding.streamlit.app/


# 📓 Google Colab
https://colab.research.google.com/drive/1F4Ey-2Mx0jtf6aF_g1qEnhM4_pLDq1rK?usp=sharing

---

# 🔗 Repository

https://github.com/wahyudwiw/uas_Bengkel_koding

---

# 🛠 Library

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

# 👨‍🎓 Author

**Wahyu Dwi Wicaksono**

NIM : A11.2023.15261

Teknik Informatika

Universitas Dian Nuswantoro


