"""
File: no30_bias_variance.py
Topic: Bias-Variance Tradeoff
Description: Demonstrates underfitting and overfitting behavior.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Bias and Variance
# ==============================
def compute_bias(y_true, y_pred):
    return np.mean((y_true - y_pred))

def compute_variance(predictions):
    return np.var(predictions)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
