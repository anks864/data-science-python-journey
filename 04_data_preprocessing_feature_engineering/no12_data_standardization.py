# ==============================
# File: no12_data_standardization.py
# Topic: Data Standardization
# Description: Standardizing data using StandardScaler
# ==============================


# ==============================
# Importing Libraries
# ==============================
import numpy as np
import pandas as pd
import sklearn

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# ==============================
# Load Dataset
# ==============================
dataset = sklearn.datasets.load_breast_cancer()

# Convert to DataFrame
df = pd.DataFrame(
    data=dataset.data,
    columns=dataset.feature_names
)

print("First five rows in the dataset:")
print(df.head())

print("Shape:", df.shape)


# ==============================
# Features and Target
# ==============================
X = df
Y = dataset.target


# ==============================
# Train-Test Split
# ==============================
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=3
)

print(
    "X.shape =", X.shape,
    "X_train.shape =", X_train.shape,
    "X_test.shape =", X_test.shape
)


# ==============================
# Before Standardization
# ==============================
print("Standard Deviation (before):", dataset.data.std())


# ==============================
# Standardization using StandardScaler
# ==============================
scaler = StandardScaler()

# Fit only on training data
scaler.fit(X_train)

# Transform data
X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)

print("Standard Deviation (after):", X_train_std.std())


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
