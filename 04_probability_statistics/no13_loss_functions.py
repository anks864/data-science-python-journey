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


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    y_true = np.array([3, 5, 7])
    y_pred = np.array([2, 5, 8])

    print("MSE:", mse(y_true, y_pred))
    # Penalizes larger errors (outliers) more strongly

    print("MAE:", mae(y_true, y_pred))
    # Treats all errors equally (impartial towards outliers)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================# 
