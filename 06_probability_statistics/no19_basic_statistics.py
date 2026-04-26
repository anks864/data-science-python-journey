# ==============================
# File: no19_statistics.py
# Topic: Statistics
# Description: Basic statistical operations to understand data
# ==============================


# ==============================
# Importing Libraries
# ==============================
import numpy as np
import pandas as pd


# ==============================
# Sample Data
# ==============================
data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Data:", data)


# ==============================
# Basic Statistics
# ==============================
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))


# ==============================
# Using Pandas
# ==============================
df = pd.DataFrame(data, columns=['Values'])

print("\nPandas Describe():")
print(df.describe())


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
