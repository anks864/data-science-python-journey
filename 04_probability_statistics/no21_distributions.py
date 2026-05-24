"""
File: no21_distributions.py
Topic: Probability Distributions
Description: Covers normal and binomial distributions, probability functions, and sampling techniques.
"""

# ==============================
# Importing Libraries
# ==============================

import numpy as np
from scipy.stats import norm, binom


# ==============================
# Normal Distribution
# ==============================

def normal_pdf(x, mean=0, std=1):
    """Probability Density Function"""
    return norm.pdf(x, mean, std)

def normal_cdf(x, mean=0, std=1):
    """Cumulative Distribution Function"""
    return norm.cdf(x, mean, std)


# ==============================
# Binomial Distribution
# ==============================

def binomial_pmf(k, n, p):
    """Probability Mass Function"""
    return binom.pmf(k, n, p)

def binomial_mean(n, p):
    return n * p

def binomial_variance(n, p):
    return n * p * (1 - p)


# ==============================
# Sampling from Distributions
# ==============================

def generate_normal_samples(size=1000, mean=0, std=1):
    return np.random.normal(mean, std, size)


# ==============================
# Example Usage
# ==============================

def example_usage():
    print("Normal PDF (x=0):", normal_pdf(0))
    print("Normal CDF (x=1.96):", normal_cdf(1.96))

    print("Binomial PMF (k=3, n=10, p=0.5):", binomial_pmf(3, 10, 0.5))
    print("Binomial Mean:", binomial_mean(10, 0.5))
    print("Binomial Variance:", binomial_variance(10, 0.5))

    samples = generate_normal_samples()
    print("Generated Sample Size:", len(samples))


# ==============================
# Execution Entry Point
# ==============================

if __name__ == "__main__":
    example_usage()


#============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#============================================================#
