"""
File: no34_model_evaluation.py
Topic: Model Evaluation Metrics
Description: Covers evaluation metrics for regression models.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Evaluation Metrics
# ==============================
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_res = np.sum((y_true - y_pred) ** 2)
    return 1 - (ss_res / ss_total)


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    y_true = np.array([3, 5, 7, 9])
    y_pred = np.array([2.5, 5, 7.5, 8])

    

#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
