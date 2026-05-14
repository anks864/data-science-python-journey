"""
File: no33_outliers_effect.py
Topic: Outliers and Their Impact
Description: Detects outliers using Z-score and IQR methods.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Z-Score Method
# ==============================
def z_score_outliers(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = (data - mean) / std
    return np.where(np.abs(z_scores) > threshold)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
