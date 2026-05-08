"""
File: no29_covariance_correlation.py
Topic: Covariance and Correlation
Description: Covers relationships between variables using covariance and Pearson correlation.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Covariance
# ==============================
def covariance(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    return np.mean((x - mean_x) * (y - mean_y))


# ==============================
# Correlation Matrix
# ==============================
def correlation_matrix(data):
    return np.corrcoef(data, rowvar=False)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
