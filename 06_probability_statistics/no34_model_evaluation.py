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


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
