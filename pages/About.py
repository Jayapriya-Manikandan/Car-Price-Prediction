import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ---------- Title ----------
st.title("ℹ️ About the Project")

st.write(
    "Learn more about the Car Price Prediction Machine Learning project."
)

st.markdown("---")


# ---------- Project Description ----------
st.markdown("## 🚗 Car Price Prediction")

st.markdown("""
This project is a **Machine Learning based used car price prediction
system**.

The application analyzes historical used-car data and predicts an
estimated selling price based on vehicle characteristics such as:

- Car name
- Present price
- Driven kilometers
- Fuel type
- Selling type
- Transmission
- Previous owners
- Car age
""")


# ---------- Technology Stack ----------
st.markdown("---")

st.markdown("## 🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🐍 Python
    Used for data processing and Machine Learning.
    """)

with col2:
    st.markdown("""
    ### 📊 Pandas
    Used for dataset handling and analysis.
    """)

with col3:
    st.markdown("""
    ### 🤖 Scikit-learn
    Used for preprocessing, model training and evaluation.
    """)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🌐 Streamlit
    Used to build the interactive web application.
    """)

with col2:
    st.markdown("""
    ### 💾 Joblib
    Used to save and load the trained Machine Learning model.
    """)


# ---------- Machine Learning Methodology ----------
st.markdown("---")

st.markdown("## 🧠 Machine Learning Methodology")

st.markdown("""
### 1. Data Preparation
The dataset is cleaned by removing duplicate records.

### 2. Feature Engineering
Car age is calculated from the manufacturing year.

### 3. Data Preprocessing
Categorical features are converted into numerical form using
**One-Hot Encoding**.

### 4. Model Training
A **Linear Regression** model is trained using the processed data.

### 5. Model Evaluation
The model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
""")


# ---------- Model Performance ----------
st.markdown("---")

st.markdown("## 📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", "1.41")

with col2:
    st.metric("RMSE", "2.43")

with col3:
    st.metric("R² Score", "0.7706")


# ---------- Project Goal ----------
st.markdown("---")

st.markdown("## 🎯 Project Goal")

st.info(
    "The goal of this project is to demonstrate how Machine Learning "
    "can be used to estimate used-car prices and provide an interactive, "
    "user-friendly prediction system."
)


# ---------- Footer ----------
st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>"
    "Car Price Prediction | Machine Learning Project"
    "</p>",
    unsafe_allow_html=True
)
