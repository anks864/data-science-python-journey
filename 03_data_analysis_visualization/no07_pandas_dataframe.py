"""
File: no07_pandas_dataframe.py
Topic: Pandas DataFrame
Description: Covers data loading, inspection, analysis, and manipulation using Pandas.
"""


# ==============================
# Importing Libraries
# ==============================

import numpy as np
import pandas as pd


# ==============================
# 1. Load Dataset (Boston Housing)
# ==============================
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)

data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
boston_target = raw_df.values[1::2, 2]

boston_df = pd.DataFrame(data, columns=[
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
])

print("Boston DataFrame (first 5 rows):\n", boston_df.head())
print("Shape:", boston_df.shape)


# ==============================
# 2. Load CSV Dataset
# ==============================
try:
    diabetes_df = pd.read_csv("diabetes.csv")
    print("Dataset loaded successfully")

    diabetes_df.to_csv("diabetes_df.csv", index=False)

except FileNotFoundError:
    print("diabetes.csv not found. Skipping this section.")


# ==============================
# 3. Create Random DataFrame
# ==============================
random_df = pd.DataFrame(np.random.rand(10, 8))
print("Random DataFrame:\n", random_df)


# ==============================
# 4. Inspect DataFrame
# ==============================
if 'diabetes_df' in locals():
    print("Shape:", diabetes_df.shape)
    print("First 5 rows:\n", diabetes_df.head())
    print("Last 5 rows:\n", diabetes_df.tail())

    print("Info:")
    diabetes_df.info()

    print("Missing values:\n", diabetes_df.isnull().sum())


# ==============================
# 5. Data Analysis
# ==============================
if 'diabetes_df' in locals():
    print("Outcome Counts:\n", diabetes_df.value_counts('Outcome'))
    print("Grouped Mean:\n", diabetes_df.groupby('Outcome').mean())

    print("Statistics:")
    print(diabetes_df.describe())


# ==============================
# 6. Data Manipulation
# ==============================
boston_df['PRICE'] = boston_target

print("After adding PRICE column:\n", boston_df.head())

print("Drop row (temporary):\n", boston_df.drop(index=0))
print("Drop column (temporary):\n", boston_df.drop(columns='ZN'))

print("Row at index 2:\n", boston_df.iloc[2])
print("Column at index 4:\n", boston_df.iloc[:, 4])


# ==============================
# 7. Correlation
# ==============================
print("Correlation Matrix:\n", boston_df.corr())


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
