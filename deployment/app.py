import streamlit as st
import pandas as pd
import joblib

# =====================================================
# LOAD MODEL & SCALER
# =====================================================

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# MAPPING
# =====================================================

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

coupon_map = {
    "NEW20": 0,
    "REF10": 1,
    "SALE15": 2
}

payment_map = {
    "BKash": 0,
    "Card": 1,
    "PayPal": 2,
    "SEPA": 3,
    "UPI": 4
}

# =====================================================
# HEADER
# =====================================================

st.title("📊 Customer Churn Prediction Dashboard")

st.caption(
    "Voting Classifier Model with Hyperparameter Tuning"
)

with st.expander("ℹ️ Informasi Model"):

    st.write("""
    Model Terbaik : Voting Classifier

    Accuracy : 83.83%
    Recall : 74.73%
    F1 Score : 55.05%

    Dataset :
    Customer Churn Dataset

    Total Feature :
    28 Feature
    """)

# =====================================================
# LAYOUT
# =====================================================

col1, col2, col3 = st.columns(3)


# =====================================================
# DEMOGRAFI
# =====================================================

with col1:

    gender = gender_map[
        st.selectbox(
            "Gender",
            ["Female", "Male", "Other"]
        )
    ]

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    country = country_map[
        st.selectbox(
            "Country",
            ["Bangladesh", "Germany", "India", "UK", "USA"]
        )
    ]

    city = city_map[
        st.selectbox(
            "City",
            [
                "Berlin",
                "Delhi",
                "Dhaka",
                "Hamburg",
                "London",
                "Mumbai",
                "New York"
            ]
        )
    ]

    signup_date = st.number_input(
        "Signup Date",
        value=100
    )

    last_purchase_date = st.number_input(
        "Last Purchase Date",
        value=10
    )

    acquisition_channel = acquisition_map[
        st.selectbox(
            "Acquisition Channel",
            [
                "Email",
                "Facebook Ads",
                "Google Ads",
                "Organic",
                "Referral"
            ]
        )
    ]

    device_type = device_map[
        st.selectbox(
            "Device Type",
            ["Desktop", "Mobile", "Tablet"]
        )
    ]

    subscription_type = subscription_map[
        st.selectbox(
            "Subscription Type",
            ["Annual", "Monthly"]
        )
    ]

# =====================================================
# AKTIVITAS
# =====================================================

with col2:

    premium_label = st.radio(
        "Premium User",
        ["No","Yes"]
    )

    is_premium_user = 1 if premium_label == "Yes" else 0

    total_visits = st.number_input(
        "Total Visits",
        value=100
    )

    avg_session_time = st.number_input(
        "Avg Session Time",
        value=30.0
    )

    pages_per_session = st.number_input(
        "Pages Per Session",
        value=5.0
    )

    email_open_rate = st.number_input(
        "Email Open Rate",
        value=0.5
    )

    email_click_rate = st.number_input(
        "Email Click Rate",
        value=0.2
    )

    total_spent = st.number_input(
        "Total Spent",
        value=1000.0
    )

    avg_order_value = st.number_input(
        "Avg Order Value",
        value=100.0
    )

    discount_label = st.radio(
        "Discount Used",
        ["No","Yes"]
    )

    discount_used = 1 if discount_label == "Yes" else 0

    coupon_code = coupon_map[
        st.selectbox(
            "Coupon Code",
            ["NEW20", "REF10", "SALE15"]
        )
    ]

# =====================================================
# KEPUASAN
# =====================================================

with col3:

    support_tickets = st.number_input(
        "Support Tickets",
        value=0
    )

    refund_label = st.radio(
        "Refund Requested",
        ["No","Yes"]
    )

    refund_requested = 1 if refund_label == "Yes" else 0

    delivery_delay_days = st.number_input(
        "Delivery Delay Days",
        value=0
    )

    payment_method = payment_map[
        st.selectbox(
            "Payment Method",
            ["BKash", "Card", "PayPal", "SEPA", "UPI"]
        )
    ]

    satisfaction_score = st.slider(
        "Satisfaction Score",
        1,
        10,
        5
    )

    nps_score = st.slider(
        "NPS Score",
        0,
        10,
        5
    )

    marketing_spend_per_user = st.number_input(
        "Marketing Spend Per User",
        value=50.0
    )

    lifetime_value = st.number_input(
        "Lifetime Value",
        value=5000.0
    )

    last_3_month_purchase_freq = st.number_input(
        "Last 3 Month Purchase Frequency",
        value=5
    )

# =====================================================
# PREDICTION
# =====================================================

st.divider()

if st.button("🔮 Prediction Analysis Result"):

    input_df = pd.DataFrame([[
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
        coupon_code,
        support_tickets,
        refund_requested,
        delivery_delay_days,
        payment_method,
        satisfaction_score,
        nps_score,
        marketing_spend_per_user,
        lifetime_value,
        last_3_month_purchase_freq
    ]], columns=[
        'gender',
        'age',
        'country',
        'city',
        'signup_date',
        'last_purchase_date',
        'acquisition_channel',
        'device_type',
        'subscription_type',
        'is_premium_user',
        'total_visits',
        'avg_session_time',
        'pages_per_session',
        'email_open_rate',
        'email_click_rate',
        'total_spent',
        'avg_order_value',
        'discount_used',
        'coupon_code',
        'support_tickets',
        'refund_requested',
        'delivery_delay_days',
        'payment_method',
        'satisfaction_score',
        'nps_score',
        'marketing_spend_per_user',
        'lifetime_value',
        'last_3_month_purchase_freq'
    ])

    # Scaling
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    try:
        probability = model.predict_proba(input_scaled)[0][1]
    except:
        probability = 0.5

    st.subheader("📊 Probability Meter")

    st.progress(float(probability))

    st.metric(
        label="Churn Probability Score",
        value=f"{probability:.2%}"
    )

    if probability >= 0.80:

        st.error("🔴 Risiko Sangat Tinggi")

    elif probability >= 0.60:

        st.warning("🟠 Risiko Tinggi")

    elif probability >= 0.40:

        st.warning("🟡 Risiko Sedang")

    else:

        st.success("🟢 Risiko Rendah")

    st.subheader("🎯 Verdict & Action Items")

    if prediction == 1:

        st.error(
            f"⚠️ Warning: Pelanggan diprediksi CHURN ({probability:.2%})"
        )
        if probability >= 0.80:

            st.warning("""
            Risiko churn sangat tinggi.

            Rekomendasi:
            - Berikan promo eksklusif
            - Hubungi pelanggan secara personal
            - Tawarkan loyalty program
            - Evaluasi pengalaman pelanggan
            """)

        elif probability >= 0.60:

            st.warning("""
            Risiko churn tinggi.

            Rekomendasi:
            - Tingkatkan engagement
            - Berikan diskon khusus
            - Tingkatkan kualitas layanan
            """)

        else:

            st.info("""
            Risiko churn sedang.

            Rekomendasi:
            - Pantau aktivitas pelanggan
            - Berikan penawaran yang relevan
            """)

    else:

        st.success(
            f"✅ Pelanggan diprediksi tetap LOYAL ({probability:.2%})"
    )

        st.info("""
        Rekomendasi Tindakan:
        - Pertahankan kualitas layanan.
        - Tingkatkan program loyalitas.
        - Tawarkan produk premium (Upselling).
        - Berikan reward kepada pelanggan aktif.
        """)

    st.subheader("📋 Input Summary")

    st.dataframe(
        input_df,
        use_container_width=True
    )