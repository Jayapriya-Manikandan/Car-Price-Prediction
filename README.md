# 🚗 Car Price Prediction using Machine Learning

A Machine Learning web application that predicts the estimated selling price of used cars based on vehicle details.

## 📌 Project Overview

This project uses historical used-car data to build a Machine Learning model for estimating car selling prices.

The application provides an interactive Streamlit interface where users can enter car details and receive an estimated selling price.

## ✨ Features

- 📊 Interactive dashboard
- 🔮 Used car price prediction
- 📈 Data analytics and visualizations
- 📋 Dataset exploration
- 🤖 Machine Learning based prediction
- 🌐 Interactive Streamlit web application

## 🧠 Machine Learning

The project uses **Linear Regression** as the prediction model.

### Data Preprocessing

- Duplicate records are removed
- Car age is calculated from the manufacturing year
- Categorical variables are converted using One-Hot Encoding
- Data is divided into training and testing sets

### Model Performance

| Metric | Value |
|---|---:|
| MAE | 1.41 |
| RMSE | 2.43 |
| R² Score | 0.7706 |

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

## 📂 Project Structure

```text
Car_Price_Prediction/
│
├── model/
│   └── car_price_model.pkl
│
├── pages/
│   ├── 1_🏠_Home.py
│   ├── 2_📊_Dashboard.py
│   ├── 3_🔮_Price_Prediction.py
│   ├── 4_📈_Analytics.py
│   ├── 5_📋_Dataset.py
│   └── 6_ℹ️_About.py
│
├── app.py
├── train_model.py
├── car_price_prediction.py
├── car data.csv
├── requirements.txt
├── .gitignore
└── README.md