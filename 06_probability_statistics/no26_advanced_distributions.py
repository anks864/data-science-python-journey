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


# ==============================
# Uniform Distribution
# ==============================
def uniform_pdf(x, a, b):
    return uniform.pdf(x, loc=a, scale=b-a)


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    print("Poisson:", poisson_pmf(3, 2))
    print("Exponential:", exponential_pdf(1, 0.5))
    print("Uniform:", uniform_pdf(2, 0, 5))


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
