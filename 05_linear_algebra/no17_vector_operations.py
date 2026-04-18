# ==============================
# File: no17_vector_operations.py
# Topic: Vector Operations
# Description: Covers visualization and operations on vectors
# ==============================


# ==============================
# Importing Libraries
# ==============================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ==============================
# Basic Vector Visualization
# ==============================
plt.quiver(0, 0, 4, 5)
plt.show()


# ==============================
# Multiple Vector Plot
# ==============================
plt.quiver(0, 0, 2, 3, scale_units='xy', angles='xy', scale='1', color='g')
plt.quiver(0, 0, 3, -2, scale_units='xy', angles='xy', scale='1', color='r')
plt.quiver(0, 0, 5, 1, scale_units='xy', angles='xy', scale='1', color='y')
plt.quiver(0, 0, -1, 5, scale_units='xy', angles='xy', scale='1', color='y')

plt.xlim(-8, 8)
plt.ylom(-8, 8)

plt.show()


# ==============================
# Vector Addition & Subtraction
# ==============================
vector_1 = np.array([0, 0, 2, 3])
vector_2 = np.array([0, 0, 3, -2])

vector_sum = vector_1 + vector_2
vector_diff = vector_1 - vector_2

print("Vector 1:", vector_1)
print("Vector 2:", vector_2)
print("Sum:", vector_sum)
print("Difference:", vector_diff)


# ==============================
# Scalar Multiplication
# ==============================
vec_1 = np.asarray([0, 0, 2, 3])

vec_2 = 2 * vec_1
vec_3 = -0.5 * vec_1

print("Original Vector:", vec_1)
print("Multiplied by 2:", vec_2)
print("Multiplied by -0.5:", vec_3)


# Visualization
plt.quiver(0, 0, 1, 2, scale_units='xy', angles='xy', scale=1, color='g')
plt.quiver(0, 0, 2, 4, scale_units='xy', angles='xy', scale=1, color='r')
plt.quiver(0, 0, -0.5, -1, scale_units='xy', angles='xy', scale=1, color='y')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.show()


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
