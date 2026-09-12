import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset",
    page_icon="📋",
    layout="wide"
)

# Load dataset
data = pd.read_csv("car data.csv")

# Remove duplicates
data = data.drop_duplicates()


# ---------- Title ----------
st.title("📋 Dataset Explorer")

st.write(
    "Explore the used car dataset used to train the Machine Learning model."
)

st.markdown("---")


# ---------- Dataset Information ----------
st.markdown("## 📊 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", data.shape[0])

with col2:
    st.metric("Columns", data.shape[1])

with col3:
    st.metric(
        "Duplicate Rows",
        0
    )


# ---------- Dataset Table ----------
st.markdown("## 🔎 Dataset Preview")

st.dataframe(
    data,
    use_container_width=True,
    height=450
)


# ---------- Statistics ----------
st.markdown("---")

st.markdown("## 📈 Statistical Summary")

st.dataframe(
    data.describe(),
    use_container_width=True
)


# ---------- Column Information ----------
st.markdown("---")

st.markdown("## 🧾 Column Information")

column_info = pd.DataFrame({
    "Column": data.columns,
    "Data Type": data.dtypes.astype(str),
    "Missing Values": data.isnull().sum().values
})

st.dataframe(
    column_info,
    use_container_width=True,
    hide_index=True
)


# ---------- Dataset Note ----------
st.markdown("---")

st.info(
    "The dataset contains information about used cars, including "
    "selling price, present price, driven kilometers, fuel type, "
    "selling type, transmission and previous ownership."
)
