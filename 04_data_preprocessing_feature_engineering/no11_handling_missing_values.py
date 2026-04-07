# ==============================
# File: no11_handling_missing_values.py
# Topic: Handling Missing Values
# Description: Covers imputation and dropping techniques
# ==============================


# ==============================
# Importing Libraries
# ==============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==============================
# Load Dataset
# ==============================
dataset = pd.read_csv("Placement_Dataset.csv")

print(dataset.head())
print("Shape of the data:", dataset.shape)

print("Number of null values in each column:")
print(dataset.isnull().sum())


# ==============================
# Imputation Techniques
# ==============================
# Central Tendencies: Mean, Median, Mode

# Analyze distribution of 'salary' column
fig, ax = plt.subplots(figsize=(8, 8))

sns.histplot(dataset['salary'], kde=True, ax=ax)

plt.show()

# Note:
# Mean is not ideal when outliers are present
# Prefer Median or Mode in such cases


# ==============================
# Imputation Using Median
# ==============================
dataset['salary'].fillna(
    dataset['salary'].median(),
    inplace=True
)

print("Number of null values after imputation:")
print(dataset.isnull().sum())

print("Sample Salary Values:")
print(dataset['salary'].head())

# To use mean/mode instead:
# dataset['salary'].mean()
# dataset['salary'].mode()[0]


# ==============================
# Dropping Missing Values
# ==============================
salary_dataset = pd.read_csv("Placement_Dataset.csv")

print("Initial shape:", salary_dataset.shape)

salary_dataset = salary_dataset.dropna(how='any')

print("Number of null values after dropping:")
print(salary_dataset.isnull().sum())

print("Final shape:", salary_dataset.shape)


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
