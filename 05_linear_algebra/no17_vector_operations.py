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
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
