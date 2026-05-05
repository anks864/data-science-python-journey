"""
File: no26_advanced_distributions.py
Topic: Probability Distributions (Advanced)
Description: Covers Poisson, Exponential, and Uniform distributions.
"""


# ==============================
# Importing Libraries
# ==============================
from scipy.stats import poisson, expon, uniform


# ==============================
# Poisson Distribution
# ==============================
def poisson_pmf(k, lam):
    return poisson.pmf(k, lam)


# ==============================
# Exponential Distribution
# ==============================
def exponential_pdf(x, rate):
    return expon.pdf(x, scale=1/rate)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
