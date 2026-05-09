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


# ==============================
# Example Simulation
# ==============================
if __name__ == "__main__":
    y_true = np.array([3, 5, 7, 9])
    y_pred_low = np.array([4, 4, 4, 4])
    y_pred_high = np.array([3, 6, 6, 10])

    print("Bias (Underfit):", compute_bias(y_true, y_pred_low))
    # Interpretation: High bias → model too simple

    print("Variance (Flexible):", compute_variance(y_pred_high))
    # Interpretation: High variance → model sensitive to data
#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
