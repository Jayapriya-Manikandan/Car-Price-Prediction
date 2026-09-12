import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

data = pd.read_csv("car data.csv")

print("=" * 60)
print("CAR PRICE PREDICTION - MODEL TRAINING")
print("=" * 60)

print(f"\nOriginal dataset shape: {data.shape}")


# ============================================================
# 2. DATA CLEANING
# ============================================================

data = data.drop_duplicates()

print(f"Dataset shape after removing duplicates: {data.shape}")


# ============================================================
# 3. FEATURE ENGINEERING
# ============================================================

# Fixed reference year for consistent predictions
reference_year = 2026

data["Car_Age"] = reference_year - data["Year"]

data = data.drop("Year", axis=1)


# ============================================================
# 4. FEATURES AND TARGET
# ============================================================

X = data.drop("Selling_Price", axis=1)
y = data["Selling_Price"]


# ============================================================
# 5. FEATURE TYPES
# ============================================================

categorical_features = [
    "Car_Name",
    "Fuel_Type",
    "Selling_type",
    "Transmission"
]

numerical_features = [
    "Present_Price",
    "Driven_kms",
    "Owner",
    "Car_Age"
]


# ============================================================
# 6. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# ============================================================
# 7. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# 8. LINEAR REGRESSION MODEL
# ============================================================

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)


# ============================================================
# 9. TRAIN MODEL
# ============================================================

print("\nTraining Linear Regression model...")

model.fit(X_train, y_train)


# ============================================================
# 10. MODEL EVALUATION
# ============================================================

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(y_test, predictions)


print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.4f}")


# ============================================================
# 11. SAVE MODEL
# ============================================================

os.makedirs("model", exist_ok=True)

model_path = "model/car_price_model.pkl"

joblib.dump(model, model_path)


print("\n" + "=" * 60)
print("MODEL SAVED SUCCESSFULLY")
print("=" * 60)

print(f"Saved to: {model_path}")
print("\nTraining completed successfully!")