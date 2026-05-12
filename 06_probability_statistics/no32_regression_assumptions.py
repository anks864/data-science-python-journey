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


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    y_true = np.array([2, 4, 6, 8])
    y_pred = np.array([2.1, 3.9, 6.2, 7.8])

    res = residuals(y_true, y_pred)
    print("Mean ~ 0:", check_mean_zero(res)) #True → residuals centered (good sign)
    print("Variance:", check_variance(res)) # Stable variance → homoscedasticity


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
