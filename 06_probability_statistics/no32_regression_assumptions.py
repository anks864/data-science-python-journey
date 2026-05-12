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


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
