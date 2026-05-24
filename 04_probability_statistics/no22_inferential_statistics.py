"""
File: no22_inferential_statistics.py
Topic: Inferential Statistics
Description: Covers sampling methods, confidence intervals, and hypothesis testing using statistical techniques.
"""

# ==============================
# Importing Libraries
# ==============================

import numpy as np
from scipy import stats


# ==============================
# Sampling Methods
# ==============================

def random_sample(data, size):
    """
    Returns a random sample without replacement.
    """
    return np.random.choice(data, size=size, replace=False)


# ==============================
# Confidence Intervals
# ==============================

def confidence_interval(data, confidence=0.95):
    """
    Computes confidence interval for the given dataset.
    """
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)

    margin = std_err * stats.t.ppf((1 + confidence) / 2., n - 1)

    return mean - margin, mean + margin


# ==============================
# Hypothesis Testing
# ==============================

def one_sample_ttest(data, population_mean):
    """
    Performs one-sample t-test.
    """
    t_stat, p_value = stats.ttest_1samp(data, population_mean)
    return t_stat, p_value

def two_sample_ttest(data1, data2):
    """
    Performs independent two-sample t-test.
    """
    t_stat, p_value = stats.ttest_ind(data1, data2)
    return t_stat, p_value


# ==============================
# Example Usage
# ==============================

if __name__ == "__main__":

    # Generate sample data
    data1 = np.random.normal(50, 10, 100)
    data2 = np.random.normal(55, 10, 100)

    # Sampling
    sample = random_sample(data1, 10)
    print("Random Sample:", sample)

    # Confidence Interval
    ci = confidence_interval(data1)
    print("Confidence Interval:", ci)

    # Hypothesis Testing
    t_stat, p_val = one_sample_ttest(data1, 50)
    print("One Sample t-test:", t_stat, p_val)

    print("Two Sample t-test:", two_sample_ttest(data1, data2))


#============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#============================================================#
