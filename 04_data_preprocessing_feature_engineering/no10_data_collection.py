# ==============================
# File: no10_data_collection.py
# Topic: Data Collection
# Description: Covers loading data from CSV files and extracting datasets
# ==============================


# ==============================
# Importing Libraries
# ==============================
import pandas as pd
from zipfile import ZipFile


# ==============================
# Dataset 1: CSV File (Housing)
# ==============================
dataset1 = pd.read_csv("housing.csv")

print("Dataset Collected:")
print(dataset1.head())


# ==============================
# API Notes: Kaggle Dataset
# ==============================
# Steps:
# 1. Install Kaggle API
# 2. Upload kaggle.json file
# 3. Configure the path of kaggle.json
# 4. Download dataset using:
#    kaggle competitions download -c LANL-Earthquake-Prediction


# ==============================
# Dataset 2: Extract ZIP Dataset
# ==============================
dataset_zip = "LANL-Earthquake-Prediction.zip"

with ZipFile(dataset_zip, 'r') as zip:
    zip.extractall()
    print("Dataset extracted successfully")


# ==============================
# Dataset 3: CSV from Extracted Files
# ==============================
print("Before data read")

dataset2 = pd.read_csv("train.csv")

print("After data read")
print("Dataset Collected:")
print(dataset2.head())


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
