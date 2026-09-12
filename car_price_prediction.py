import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

data = pd.read_csv("car data.csv")

print("=" * 60)
print("CAR PRICE PREDICTION")
print("=" * 60)

print("\nOriginal Dataset Shape:")
print(data.shape)


# ============================================================
# 2. DATA CLEANING
# ============================================================

# Remove duplicate rows
data = data.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())


# ============================================================
# 3. FEATURE ENGINEERING
# ============================================================

# Create car age from manufacturing year
current_year = 2026
data["Car_Age"] = current_year - data["Year"]

# Remove original year column because Car_Age is more meaningful
data = data.drop("Year", axis=1)

print("\nFeatures After Engineering:")
print(data.columns.tolist())


# ============================================================
# 4. EXPLORATORY DATA ANALYSIS
# ============================================================

# Selling price distribution
plt.figure(figsize=(8, 5))
plt.hist(data["Selling_Price"], bins=30)
plt.xlabel("Selling Price")
plt.ylabel("Number of Cars")
plt.title("Distribution of Car Selling Prices")
plt.tight_layout()
plt.show()


# Selling price vs present price
plt.figure(figsize=(8, 5))
plt.scatter(data["Present_Price"], data["Selling_Price"], alpha=0.6)
plt.xlabel("Present Price")
plt.ylabel("Selling Price")
plt.title("Present Price vs Selling Price")
plt.tight_layout()
plt.show()


# Selling price vs driven kilometers
plt.figure(figsize=(8, 5))
plt.scatter(data["Driven_kms"], data["Selling_Price"], alpha=0.6)
plt.xlabel("Driven Kilometers")
plt.ylabel("Selling Price")
plt.title("Driven Kilometers vs Selling Price")
plt.tight_layout()
plt.show()


# ============================================================
# 5. DEFINE FEATURES AND TARGET
# ============================================================

X = data.drop("Selling_Price", axis=1)
y = data["Selling_Price"]


# ============================================================
# 6. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
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
# 7. PREPROCESSING
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
# 8. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# 9. LINEAR REGRESSION MODEL
# ============================================================

linear_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_rmse = mean_squared_error(
    y_test,
    linear_predictions
) ** 0.5
linear_r2 = r2_score(y_test, linear_predictions)


# ============================================================
# 10. RANDOM FOREST REGRESSION MODEL
# ============================================================

random_forest_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=300,
                random_state=42
            )
        )
    ]
)

random_forest_model.fit(X_train, y_train)

rf_predictions = random_forest_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_rmse = mean_squared_error(
    y_test,
    rf_predictions
) ** 0.5
rf_r2 = r2_score(y_test, rf_predictions)


# ============================================================
# 11. MODEL COMPARISON
# ============================================================

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print("\nLinear Regression:")
print(f"MAE  : {linear_mae:.2f}")
print(f"RMSE : {linear_rmse:.2f}")
print(f"R2   : {linear_r2:.4f}")

print("\nRandom Forest Regression:")
print(f"MAE  : {rf_mae:.2f}")
print(f"RMSE : {rf_rmse:.2f}")
print(f"R2   : {rf_r2:.4f}")


# ============================================================
# 12. SELECT BEST MODEL
# ============================================================

if rf_r2 >= linear_r2:
    best_model = random_forest_model
    best_predictions = rf_predictions
    best_model_name = "Random Forest Regression"
    best_r2 = rf_r2
else:
    best_model = linear_model
    best_predictions = linear_predictions
    best_model_name = "Linear Regression"
    best_r2 = linear_r2


print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Selected Model: {best_model_name}")
print(f"R2 Score: {best_r2:.4f}")


# ============================================================
# 13. ACTUAL VS PREDICTED PRICE
# ============================================================

plt.figure(figsize=(8, 5))
plt.scatter(y_test, best_predictions, alpha=0.7)

# Perfect prediction reference line
min_price = min(y_test.min(), best_predictions.min())
max_price = max(y_test.max(), best_predictions.max())

plt.plot(
    [min_price, max_price],
    [min_price, max_price]
)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title(f"Actual vs Predicted Price - {best_model_name}")
plt.tight_layout()
plt.show()


# ============================================================
# 14. SAMPLE PRICE PREDICTION
# ============================================================

sample_car = pd.DataFrame({
    "Car_Name": ["city"],
    "Present_Price": [8.5],
    "Driven_kms": [30000],
    "Fuel_Type": ["Petrol"],
    "Selling_type": ["Dealer"],
    "Transmission": ["Manual"],
    "Owner": [0],
    "Car_Age": [5]
})

predicted_price = best_model.predict(sample_car)[0]

print("\n" + "=" * 60)
print("SAMPLE CAR PRICE PREDICTION")
print("=" * 60)

print(f"Predicted Selling Price: ₹{predicted_price:.2f} Lakhs")

print("\nProject execution completed successfully!")