"""
File: no31_loss_functions.py
Topic: Loss Functions
Description: Covers MSE and MAE used in regression.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Loss Functions
# ==============================
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================# 
