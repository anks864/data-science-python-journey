"""
File: no20_probability_basics.py
Topic: Probability Basics
Description: Covers fundamental probability concepts, simulations, conditional probability, and independence.
"""

# ==============================
# Importing Libraries
# ==============================

import random


# ==============================
# Basic Probability
# ==============================

def probability(event_outcomes, total_outcomes):
    return event_outcomes / total_outcomes


# ==============================
# Coin Toss Simulation
# ==============================

def simulate_coin_toss(trials=1000):
    heads = 0

    for _ in range(trials):
        if random.choice(['H', 'T']) == 'H':
            heads += 1

    return heads / trials


# ==============================
# Dice Simulation
# ==============================

def simulate_dice_roll(trials=1000):
    count = 0

    for _ in range(trials):
        if random.randint(1, 6) == 6:
            count += 1

    return count / trials


# ==============================
# Conditional Probability
# ==============================

def conditional_probability(p_a_and_b, p_b):
    if p_b == 0:
        return 0
    return p_a_and_b / p_b


# ==============================
# Independence Check
# ==============================

def are_independent(p_a, p_b, p_a_and_b):
    return abs(p_a * p_b - p_a_and_b) < 1e-6


# ==============================
# Example Usage
# ==============================

def example():
    print("P(rolling a 3 on dice):", probability(1, 6))
    print("Coin Toss Simulation:", simulate_coin_toss())
    print("Dice Roll Simulation:", simulate_dice_roll())

    p_a = 0.5
    p_b = 0.4
    p_a_and_b = 0.2

    print("Conditional Probability:", conditional_probability(p_a_and_b, p_b))
    print("Are Events Independent:", are_independent(p_a, p_b, p_a_and_b))


# ==============================
# Execution
# ==============================

if __name__ == "__main__":
    example()


#============================================================#
# EOF: Feel free to open an issue to report a bug or discrepancy
#============================================================#
