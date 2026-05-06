"""
File: no27_sampling_and_estimations.py
Topic: Sampling and Parameter Estimation
Description: Covers sampling techniques and estimation methods like MLE.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Sampling Techniques
# ==============================
def simple_random_sample(data, size):
    return np.random.choice(data, size=size, replace=False)


# ==============================
# Parameter Estimation
# ==============================
def estimate_mean(data):
    return np.mean(data)

def estimate_variance(data):
    return np.var(data)


# ==============================
# Maximum Likelihood (Normal)
# ==============================
def mle_normal(data):
    mu = np.mean(data)
    sigma = np.std(data)
    return mu, sigma


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    data = np.random.normal(10, 2, 100)

    print("Sample:", simple_random_sample(data, 5))
    # Subset representing the population
    print("Mean Estimate:", estimate_mean(data))
    # Best estimate of population mean
    print("MLE:", mle_normal(data))
    # Parameters (μ, σ) that best fit the data


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
