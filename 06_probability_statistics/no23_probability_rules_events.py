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
#==============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#==============================================================#
