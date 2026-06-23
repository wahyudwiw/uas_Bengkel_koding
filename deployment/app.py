import streamlit as st
import pandas as pd
import joblib

# LOAD MODEL


model = joblib.load("best_model.pkl")

# KONFIGURASI HALAMAN


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.markdown("""
Aplikasi ini digunakan untuk memprediksi apakah seorang pelanggan
berpotensi melakukan **Churn** atau **Tidak Churn**
berdasarkan karakteristik dan aktivitas pelanggan.
""")

# INPUT DATA

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    country = st.selectbox(
        "Country",
        ["India", "Germany", "USA", "UK", "Bangladesh"]
    )

    city = st.selectbox(
        "City",
        [
            "Berlin",
            "Mumbai",
            "London",
            "Hamburg",
            "New York",
            "Delhi",
            "Dhaka"
        ]
    )

    acquisition_channel = st.selectbox(
        "Acquisition Channel",
        [
            "Email",
            "Organic",
            "Facebook Ads",
            "Referral",
            "Google Ads"
        ]
    )

    device_type = st.selectbox(
        "Device Type",
        [
            "Tablet",
            "Desktop",
            "Mobile"
        ]
    )

    subscription_type = st.selectbox(
        "Subscription Type",
        [
            "Annual",
            "Monthly"
        ]
    )

    is_premium_user = st.selectbox(
        "Premium User",
        [0, 1]
    )

    total_visits = st.number_input(
        "Total Visits",
        min_value=0,
        value=15
    )

    avg_session_time = st.number_input(
        "Average Session Time",
        min_value=0.0,
        value=8.0
    )

    pages_per_session = st.number_input(
        "Pages Per Session",
        min_value=0.0,
        value=4.0
    )

    email_open_rate = st.slider(
        "Email Open Rate",
        0.0,
        1.0,
        0.5
    )

    email_click_rate = st.slider(
        "Email Click Rate",
        0.0,
        1.0,
        0.2
    )

with col2:

    total_spent = st.number_input(
        "Total Spent",
        min_value=0.0,
        value=1000.0
    )

    avg_order_value = st.number_input(
        "Average Order Value",
        min_value=0.0,
        value=50.0
    )

    discount_used = st.selectbox(
        "Discount Used",
        [0, 1]
    )

    support_tickets = st.number_input(
        "Support Tickets",
        min_value=0,
        value=2
    )

    refund_requested = st.selectbox(
        "Refund Requested",
        [0, 1]
    )

    delivery_delay_days = st.number_input(
        "Delivery Delay Days",
        min_value=0,
        value=2
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "UPI",
            "BKash",
            "PayPal",
            "SEPA",
            "Card"
        ]
    )

    satisfaction_score = st.slider(
        "Satisfaction Score",
        1,
        5,
        4
    )

    nps_score = st.slider(
        "NPS Score",
        0,
        10,
        7
    )

    marketing_spend_per_user = st.number_input(
        "Marketing Spend Per User",
        min_value=0.0,
        value=15.0
    )

    lifetime_value = st.number_input(
        "Lifetime Value",
        min_value=0.0,
        value=1200.0
    )

    last_3_month_purchase_freq = st.number_input(
        "Last 3 Month Purchase Frequency",
        min_value=0,
        value=6
    )

# ENCODING MANUAL

gender_map = {
    "Female": 0,
    "Male": 1,
    "Other": 2
}

country_map = {
    "Bangladesh": 0,
    "Germany": 1,
    "India": 2,
    "UK": 3,
    "USA": 4
}

city_map = {
    "Berlin": 0,
    "Delhi": 1,
    "Dhaka": 2,
    "Hamburg": 3,
    "London": 4,
    "Mumbai": 5,
    "New York": 6
}

acquisition_map = {
    "Email": 0,
    "Facebook Ads": 1,
    "Google Ads": 2,
    "Organic": 3,
    "Referral": 4
}

device_map = {
    "Desktop": 0,
    "Mobile": 1,
    "Tablet": 2
}

subscription_map = {
    "Annual": 0,
    "Monthly": 1
}

payment_map = {
    "BKash": 0,
    "Card": 1,
    "PayPal": 2,
    "SEPA": 3,
    "UPI": 4
}

# Encode

gender = gender_map[gender]
country = country_map[country]
city = city_map[city]
acquisition_channel = acquisition_map[acquisition_channel]
device_type = device_map[device_type]
subscription_type = subscription_map[subscription_type]
payment_method = payment_map[payment_method]

# Karena model lama memakai LabelEncoder untuk tanggal
signup_date = 100
last_purchase_date = 200

# PREDIKSI

if st.button("🔍 Prediksi Churn"):

    input_data = pd.DataFrame([[
        gender,
        age,
        country,
        city,
        signup_date,
        last_purchase_date,
        acquisition_channel,
        device_type,
        subscription_type,
        is_premium_user,
        total_visits,
        avg_session_time,
        pages_per_session,
        email_open_rate,
        email_click_rate,
        total_spent,
        avg_order_value,
        discount_used,
        support_tickets,
        refund_requested,
        delivery_delay_days,
        payment_method,
        satisfaction_score,
        nps_score,
        marketing_spend_per_user,
        lifetime_value,
        last_3_month_purchase_freq
    ]])

    prediction = model.predict(input_data)

    st.subheader("Hasil Prediksi")

    if prediction[0] == 1:
        st.error("⚠️ Customer Diprediksi CHURN")
    else:
        st.success("✅ Customer Diprediksi TIDAK CHURN")

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_data)

        st.subheader("Probabilitas")

        st.write(
            f"Churn : {prob[0][1]*100:.2f}%"
        )

        st.write(
            f"Tidak Churn : {prob[0][0]*100:.2f}%"
        )

# FOOTER

st.markdown("---")
st.caption("UAS Machine Learning - Customer Churn Prediction")