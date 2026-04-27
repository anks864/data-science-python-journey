"""
File: no19_descriptive_statistics.py
Topic: Descriptive Statistics
Description: Covers measures of central tendency, variability, percentiles, and dataset summarization.
"""

# ==============================
# Importing Libraries
# ==============================

import numpy as np
from collections import Counter


# ==============================
# Sample Dataset
# ==============================

data = [12, 15, 14, 10, 18, 21, 18, 15, 14, 13]


# ==============================
# Measures of Central Tendency
# ==============================

def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def mode(data):
    frequency = Counter(data)
    max_freq = max(frequency.values())
    return [k for k, v in frequency.items() if v == max_freq]


# ==============================
# Measures of Variability
# ==============================

def data_range(data):
    return max(data) - min(data)


def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def standard_deviation(data):
    return np.sqrt(variance(data))


# ==============================
# Percentiles and Quartiles
# ==============================

def percentile(data, p):
    return np.percentile(data, p)


def quartiles(data):
    return {
        "Q1": percentile(data, 25),
        "Q2": percentile(data, 50),
        "Q3": percentile(data, 75)
    }


# ==============================
# Summary Function
# ==============================

def describe(data):
    return {
        "Mean": mean(data),
        "Median": median(data),
        "Mode": mode(data),
        "Range": data_range(data),
        "Variance": variance(data),
        "Std Dev": standard_deviation(data),
        "Quartiles": quartiles(data)
    }


# ==============================
# Example Usage
# ==============================

def example_usage():
    summary = describe(data)

    print("Descriptive Statistics Summary:\n")
    for key, value in summary.items():
        print(f"{key}: {value}")


# ==============================
# Execution Entry Point
# ==============================

if __name__ == "__main__":
    example_usage()


#============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#============================================================#
