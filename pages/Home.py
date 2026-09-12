import streamlit as st

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .main-title {
        font-size: 45px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .info-box {
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.3);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Title ----------
st.markdown(
    '<div class="main-title">🚗 Car Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Used Car Price Estimation System</div>',
    unsafe_allow_html=True
)


# ---------- Introduction ----------
st.markdown("## 📌 Project Overview")

st.markdown("""
<div class="info-box">

This project uses **Machine Learning** to estimate the selling price of
used cars based on important vehicle details such as present price,
driven kilometers, fuel type, transmission, ownership and car age.

The system is built using **Python, Pandas, Scikit-learn and Streamlit**.

</div>
""", unsafe_allow_html=True)


# ---------- Key Highlights ----------
st.markdown("## ✨ Key Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Size", "301 Cars")

with col2:
    st.metric("ML Model", "Linear Regression")

with col3:
    st.metric("R² Score", "0.7706")

with col4:
    st.metric("Prediction Unit", "₹ Lakhs")


# ---------- Features ----------
st.markdown("## 🛠️ What You Can Do")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Explore the Data
    - View dataset information
    - Analyze car prices
    - Explore fuel and transmission types
    - Understand important patterns
    """)

with col2:
    st.markdown("""
    ### 🔮 Predict Car Price
    - Enter car details
    - Use the trained ML model
    - Get an estimated selling price
    - Make data-driven decisions
    """)


# ---------- Navigation ----------
st.markdown("## 🧭 Explore the Application")

st.info(
    "Use the pages in the sidebar to explore the Dashboard, "
    "Price Prediction, Analytics, Dataset and Project information."
)


# ---------- Footer ----------
st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>"
    "Car Price Prediction | Machine Learning Project"
    "</p>",
    unsafe_allow_html=True
)
