"""
File: no32_regression_assumptions.py
Topic: Regression Assumptions
Description: Checks basic assumptions like linearity and residual distribution.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Residuals
# ==============================
def residuals(y_true, y_pred):
    return y_true - y_pred


# ==============================
# Assumption Checks
# ==============================
def check_mean_zero(res):
    return np.isclose(np.mean(res), 0, atol=1e-2)

def check_variance(res):
    return np.var(res)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
