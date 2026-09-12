import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

# Load dataset
data = pd.read_csv("car data.csv")
data = data.drop_duplicates()

# Create car age
data["Car_Age"] = 2026 - data["Year"]


# ---------- Title ----------
st.title("📈 Car Price Analytics")

st.write(
    "Visual analysis of factors affecting used car selling prices."
)

st.markdown("---")


# ---------- 1. Selling Price Distribution ----------
st.markdown("## 💰 Selling Price Distribution")

fig, ax = plt.subplots()

ax.hist(data["Selling_Price"], bins=20)

ax.set_xlabel("Selling Price (₹ Lakhs)")
ax.set_ylabel("Number of Cars")
ax.set_title("Distribution of Selling Prices")

st.pyplot(fig)

st.markdown("---")


# ---------- 2. Present Price vs Selling Price ----------
st.markdown("## 💵 Present Price vs Selling Price")

fig, ax = plt.subplots()

ax.scatter(
    data["Present_Price"],
    data["Selling_Price"],
    alpha=0.7
)

ax.set_xlabel("Present Price (₹ Lakhs)")
ax.set_ylabel("Selling Price (₹ Lakhs)")
ax.set_title("Present Price vs Selling Price")

st.pyplot(fig)

st.markdown("---")


# ---------- 3. Selling Price by Fuel Type ----------
st.markdown("## ⛽ Selling Price by Fuel Type")

fuel_price = data.groupby("Fuel_Type")["Selling_Price"].mean()

fig, ax = plt.subplots()

fuel_price.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Fuel Type")
ax.set_ylabel("Average Selling Price (₹ Lakhs)")
ax.set_title("Average Selling Price by Fuel Type")

st.pyplot(fig)

st.markdown("---")


# ---------- 4. Selling Price by Transmission ----------
st.markdown("## ⚙️ Selling Price by Transmission")

transmission_price = data.groupby("Transmission")["Selling_Price"].mean()

fig, ax = plt.subplots()

transmission_price.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Transmission")
ax.set_ylabel("Average Selling Price (₹ Lakhs)")
ax.set_title("Average Selling Price by Transmission")

st.pyplot(fig)

st.markdown("---")


# ---------- 5. Driven KM vs Selling Price ----------
st.markdown("## 🛣️ Driven Kilometers vs Selling Price")

fig, ax = plt.subplots()

ax.scatter(
    data["Driven_kms"],
    data["Selling_Price"],
    alpha=0.7
)

ax.set_xlabel("Driven Kilometers")
ax.set_ylabel("Selling Price (₹ Lakhs)")
ax.set_title("Driven Kilometers vs Selling Price")

st.pyplot(fig)

st.markdown("---")


# ---------- 6. Car Age vs Selling Price ----------
st.markdown("## 📅 Car Age vs Selling Price")

fig, ax = plt.subplots()

ax.scatter(
    data["Car_Age"],
    data["Selling_Price"],
    alpha=0.7
)

ax.set_xlabel("Car Age (Years)")
ax.set_ylabel("Selling Price (₹ Lakhs)")
ax.set_title("Car Age vs Selling Price")

st.pyplot(fig)


# ---------- Summary ----------
st.markdown("---")

st.markdown("## 📝 Key Insights")

st.info(
    """
    • Present Price has a strong relationship with Selling Price.

    • Selling prices vary across different fuel types.

    • Transmission type can influence the average selling price.

    • Higher driven kilometers generally affect resale value.

    • Older cars tend to have lower selling prices.
    """
)
