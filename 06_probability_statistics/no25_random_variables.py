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


# ==============================
# Discrete Random Variable Example
# ==============================
def dice_expectation():
    values = np.array([1, 2, 3, 4, 5, 6])
    probabilities = np.ones(6) / 6
    return expectation(values, probabilities)


# ==============================
# Continuous Approximation
# ==============================
def continuous_mean(samples):
    return np.mean(samples)


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    print("Dice Expectation:", dice_expectation())
    # Interpretation: Long-run average outcome of dice rolls (~3.5)
    samples = np.random.normal(0, 1, 1000)
    print("Approx Mean:", continuous_mean(samples))
    # Interpretation: Estimated mean approaches true mean as sample size increases


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
