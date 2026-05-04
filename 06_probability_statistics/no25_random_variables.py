"""
File: no25_random_variables.py
Topic: Random Variables
Description: Covers discrete and continuous random variables, expectation, and variance.
"""

# ==============================
# Importing Libraries
# ==============================
import numpy as np

# ==============================
# Expectation and Variance
# ==============================
def expectation(values, probabilities):
    return np.sum(values * probabilities)

def variance(values, probabilities):
    mean = expectation(values, probabilities)
    return np.sum(probabilities * (values - mean) ** 2)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
