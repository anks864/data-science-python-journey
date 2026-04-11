# ==============================
# File: no15_handling_imbalanced_dataset.py
# Topic: Handling Imbalanced Dataset
# Description: Uses under-sampling to balance class distribution
# ==============================


# ==============================
# Importing Libraries
# ==============================
import numpy as np
import pandas as pd


# ==============================
# Load Dataset: Credit Card Data
# ==============================
credit_card_data = pd.read_csv("credit_data.csv")

print("First five rows:")
print(credit_card_data.head())

print("Last five rows:")
print(credit_card_dataset.tail())


# ==============================
# Class Distribution
# ==============================
print("Value counts:\n", credit_card_data['Class'].value_counts())

# 0 -> Legit Transactions
# 1 -> Fraudulent Transactions


# ==============================
# Separate Classes
# ==============================
legit = credit_card_data[credit_card_data['Class'] == 0]
fraud = credit_card_data[credit_card_data['Class'] == 1]

print("Shape of Legit Data:", legit.shape)
print("Shape of Fraud Data:", fraud.shape)


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
