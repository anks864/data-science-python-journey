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


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
