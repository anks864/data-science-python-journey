# ==============================
# File: no14_train_test_split.py
# Topic: Train-Test Split
# Description: Preprocessing numerical data and splitting dataset
# ==============================


# ==============================
# Importing Libraries
# ==============================
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# ==============================
# Load Dataset: PIMA Diabetes
# ==============================
diabetes_dataset = pd.read_csv("diabetes.csv")

print("First five rows:")
print(diabetes_dataset.head())

print("Shape of data:", diabetes_dataset.shape)

print("Statistical measures:")
print(diabetes_dataset.describe())

print("Outcome value counts:")
print(diabetes_dataset['Outcome'].value_counts())

# 0 -> Non-Diabetic
# 1 -> Diabetic

print("Grouped mean by Outcome:")
print(diabetes_dataset.groupby('Outcome').mean())


# ==============================
# Separate Features and Labels
# ==============================
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']


# ==============================
# Standardization
# ==============================
scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print("Standardized Data:")
print(standardized_data)

# Replace X with standardized data
X = standardized_data


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
