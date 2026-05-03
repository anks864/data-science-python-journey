"""
File: no24_bayes_theorem.py
Topic: Bayes Theorem
Description: Covers conditional probability and Bayesian inference with practical examples.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Bayes Theorem
# ==============================
def bayes_theorem(p_b_given_a, p_a, p_b):
    return (p_b_given_a * p_a) / p_b


# ==============================
# Example: Medical Testing
# ==============================

def medical_test_example():
    p_disease = 0.01
    p_positive_given_disease = 0.99
    p_positive = 0.05

    return bayes_theorem(p_positive_given_disease, p_disease, p_positive)


# ==============================
# Naive Bayes (Simplified)
# ==============================

def naive_bayes(priors, likelihoods):
    posterior = priors * likelihoods
    return posterior / np.sum(posterior)


# ==============================
# Example Usage
# ==============================

if __name__ == "__main__":
    print("Posterior (Medical):", medical_test_example())

    priors = np.array([0.6, 0.4])
    likelihoods = np.array([0.7, 0.2])

    print("Naive Bayes:", naive_bayes(priors, likelihoods))


#============================================================#
# EOF
#============================================================#
