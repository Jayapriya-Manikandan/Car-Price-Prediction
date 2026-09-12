import streamlit as st

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

st.title(" Car Price Prediction")

st.markdown("""
## Welcome

This is a Machine Learning based **Used Car Price Prediction System**.

Use the navigation menu on the left to explore:

- 🏠 **Home** — Project overview
- 📊 **Dashboard** — Dataset statistics
- 🔮 **Price Prediction** — Predict a car's selling price
- 📈 **Analytics** — Explore data patterns and visualizations
- 📋 **Dataset** — View and explore the dataset
- ℹ️ **About** — Project methodology and model information
""")

st.markdown("---")

st.info(
    "Select a page from the sidebar to get started."
)

st.markdown(
    "<p style='text-align:center;'>"
    "Machine Learning • Python • Scikit-learn • Streamlit"
    "</p>",
    unsafe_allow_html=True
)