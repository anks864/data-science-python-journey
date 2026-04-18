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
plt.quiver(0, 0, 2, 3, scale_units='xy', angles='xy', scale=1, color='g')
plt.quiver(0, 0, 3, -2, scale_units='xy', angles='xy', scale=1, color='r')
plt.quiver(0, 0, 5, 1, scale_units='xy', angles='xy', scale=1, color='y')
plt.quiver(0, 0, -1, 5, scale_units='xy', angles='xy', scale=1, color='y')

plt.xlim(-8, 8)
plt.ylim(-8, 8)

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
# Dot Product & Cross Product
# ==============================
a = np.array([2, 3])
b = np.array([4, 4])

a_dot_b = np.dot(a, b)
a_cross_b = np.cross(a, b)

print("A:", a)
print("B:", b)
print("Dot Product (A · B):", a_dot_b)
print("Cross Product (A x B):", a_cross_b)


# 3D Vectors
c = np.array([40, 20, 35])
d = np.array([53, 24, 68])

c_dot_d = np.dot(c, d)
c_cross_d = np.cross(c, d)

print("\nC:", c[0], "i +", c[1], "j +", c[2], "k")
print("D:", d[0], "i +", d[1], "j +", d[2], "k")
print("Dot Product (C · D):", c_dot_d)
print("Cross Product (C x D):", c_cross_d)


# ==============================
# Projection of Vectors
# ==============================
# 2D Example
a1 = np.array([2, 5])
b1 = np.array([8, -6])

projection_a1_on_b1 = (np.dot(a1, b1) / np.sum(b1**2)) * b1

print("\nVector A:", a1[0], "i +", a1[1], "j")
print("Vector B:", b1[0], "i +", b1[1], "j")
print("Projection of A on B:", projection_a1_on_b1)


# 3D Example
a2 = np.array([23, 45, 62])
b2 = np.array([45, 82, 67])

projection_a2_on_b2 = (np.dot(a2, b2) / np.sum(b2**2)) * b2

print("\nVector A:", a2[0], "i +", a2[1], "j +", a2[2], "k")
print("Vector B:", b2[0], "i +", b2[1], "j +", b2[2], "k")
print("Projection of A on B:", projection_a2_on_b2)


# Alternate Projection (using magnitude)
a3 = np.array([2, 5])
b3 = np.array([8, -6])

magn_b3 = np.sqrt(np.sum(b3**2))

projection_a3_on_b3 = (np.dot(a3, b3) / magn_b3**2) * b3

print("\nVector A:", a3[0], "i +", a3[1], "j")
print("Vector B:", b3[0], "i +", b3[1], "j")
print("Projection of A on B:", projection_a3_on_b3)


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
