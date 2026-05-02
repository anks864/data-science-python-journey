"""
File: no23_probability_rules_events.py
Topic: Probability Rules and Types of Events
Description: Covers probability axioms, event types, and fundamental probability rules.
"""

# ==============================
# Importing Libraries
# ==============================
import itertools


# ==============================
# Basic Probability Rules
# ==============================
def probability(event_outcomes, total_outcomes):
    return event_outcomes / total_outcomes

def complement(p_a):
    return 1 - p_a


# ==============================
# Event Relationships
# ==============================
def union(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b

def intersection_independent(p_a, p_b):
    return p_a * p_b


# ==============================
# Types of Events
# ==============================
def are_mutually_exclusive(p_a_and_b):
    return p_a_and_b == 0

def are_independent(p_a, p_b, p_a_and_b):
    return abs(p_a * p_b - p_a_and_b) < 1e-6


# ==============================
# Sample Space Example
# ==============================
def sample_space_dice():
    return list(itertools.product(range(1, 7), repeat=2))


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    print("P(A or B):", union(0.5, 0.4, 0.2))
    print("Independent:", are_independent(0.5, 0.4, 0.2))
    print("Sample Space Size:", len(sample_space_dice()))


#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
