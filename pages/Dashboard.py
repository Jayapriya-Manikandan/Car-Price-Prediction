import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
data = pd.read_csv("car data.csv")

# Remove duplicates
data = data.drop_duplicates()

# Create car age
data["Car_Age"] = 2026 - data["Year"]


# ---------- Title ----------
st.title("📊 Car Price Dashboard")
st.write("Explore key statistics and insights from the used car dataset.")


# ---------- KPI Cards ----------
st.markdown("## 📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Cars",
        len(data)
    )

with col2:
    st.metric(
        "Average Selling Price",
        f"₹{data['Selling_Price'].mean():.2f} L"
    )

with col3:
    st.metric(
        "Average Present Price",
        f"₹{data['Present_Price'].mean():.2f} L"
    )

with col4:
    st.metric(
        "Average Driven KM",
        f"{data['Driven_kms'].mean():,.0f}"
    )


# ---------- Price Information ----------
st.markdown("## 💰 Price Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Minimum Selling Price",
        f"₹{data['Selling_Price'].min():.2f} L"
    )

with col2:
    st.metric(
        "Maximum Selling Price",
        f"₹{data['Selling_Price'].max():.2f} L"
    )

with col3:
    st.metric(
        "Median Selling Price",
        f"₹{data['Selling_Price'].median():.2f} L"
    )


# ---------- Dataset Insights ----------
st.markdown("## 🔍 Dataset Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⛽ Fuel Type")

    fuel_counts = data["Fuel_Type"].value_counts()

    st.bar_chart(fuel_counts)


with col2:
    st.markdown("### ⚙️ Transmission")

    transmission_counts = data["Transmission"].value_counts()

    st.bar_chart(transmission_counts)


# ---------- Selling Type ----------
st.markdown("### 🏷️ Selling Type")

selling_type_counts = data["Selling_type"].value_counts()

st.bar_chart(selling_type_counts)


# ---------- Summary ----------
st.markdown("## 📝 Summary")

st.info(
    "The dashboard provides a quick overview of the used car dataset, "
    "including price statistics, fuel types, transmission types and "
    "selling methods."
)
