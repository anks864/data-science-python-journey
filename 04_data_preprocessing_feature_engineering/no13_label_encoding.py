# ==============================
# File: no13_label_encoding.py
# Topic: Label Encoding
# Description: Converts categorical labels into numeric form
# ==============================


# ==============================
# Importing Libraries
# ==============================
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# ==============================
# Example 1: Cancer Dataset (Commented)
# ==============================
'''
cancer_data = pd.read_csv("breast_cancer_data.csv")

print("First five rows:")
print(cancer_data.head())

# Count of different labels
print("Diagnosis value counts:")
print(cancer_data['diagnosis'].value_counts())

# Apply Label Encoding
label_encode = LabelEncoder()
labels = label_encode.fit_transform(cancer_data['diagnosis'])

# Add encoded labels to DataFrame
cancer_data['target'] = labels

# Note:
# 0 -> Benign
# 1 -> Malignant (alphabetical order)

print("Updated first five rows:")
print(cancer_data.head())

print(cancer_data['target'].value_counts())
'''


# ==============================
# Example 2: Iris Dataset
# ==============================
iris_data = pd.read_csv("iris_data.csv")

print("First five rows:")
print(iris_data.head())

print("Species value counts:")
print(iris_data['Species'].value_counts())


# ==============================
# Apply Label Encoding
# ==============================
label_encode_iris = LabelEncoder()

iris_labels = label_encode_iris.fit_transform(
    iris_data['Species']
)

iris_data['target'] = iris_labels

print("Updated first five rows:")
print(iris_data.head())

print("Encoded label counts:")
print(iris_data['target'].value_counts())


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
