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


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    print("Covariance:", covariance(x, y))
    # Interpretation: Positive → variables increase together

    print("Correlation:", correlation(x, y))
    # Interpretation: Close to 1 → strong linear relationship

    print("Correlation Matrix:\n", correlation_matrix([x, y]))
    # Interpretation: Diagonal = 1, off-diagonal shows relationships


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
