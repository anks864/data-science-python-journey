"""
File: no28_distance_measures.py
Topic: Measures of Distance
Description: Covers Euclidean, Manhattan, and Cosine distance used in ML.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Distance Measures
# ==============================
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def cosine_distance(a, b):
    return 1 - cosine_similarity(a, b)


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
