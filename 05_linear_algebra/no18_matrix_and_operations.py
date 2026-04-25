# ==============================
# File: no18_matrix_and_operations.py
# Topic: Matrix and Operations
# Description: Covers matrix creation and basic operations using NumPy
# ==============================


# ==============================
# Importing Libraries
# ==============================
import numpy as np


# ==============================
# Matrix Basics
# ==============================
# Scalar  -> Single number (1 x 1)
# Vector  -> List of numbers (row/column) (1 x n) or (n x 1)
# Matrix  -> Collection of rows and columns (m x n)


# ==============================
# Creating Matrices
# ==============================
matrix_1 = np.array([
    [10, 35, 45],
    [50, 64, 80],
    [20, 15, 90]
])

print("Matrix 1:")
print(matrix_1)

print("Shape:", matrix_1.shape)


# ==============================
# Random Matrices
# ==============================
random_matrix = np.random.rand(4, 4)

print("Random Matrix:")
print(random_matrix)

# Random Integer Matrix
random_int_matrix = np.random.randint(
    50, 100,
    size=(4, 5)
)

print("Random Integer Matrix:")
print(random_int_matrix)


# ==============================
# Special Matrices
# ==============================
# Ones Matrix
matrix_3 = np.ones((2, 3))
matrix_4 = np.ones((2, 3), dtype=int)

print("Unit Matrix (Float):")
print(matrix_3)

print("Unit Matrix (Int):")
print(matrix_4)

# Zero Matrix
null_matrix_1 = np.zeros((6, 3))
null_matrix_2 = np.zeros((6, 3), dtype=int)

print("Null Matrix (Float):")
print(null_matrix_1)

print("Null Matrix (Int):")
print(null_matrix_2)

# Identity Matrix
identity_matrix = np.eye(4, 4, dtype=int)

print("Identity Matrix:")
print(identity_matrix)


# ==============================
# Transpose of a Matrix
# ==============================
a = np.random.randint(20, 80, size=(5, 3))

print("Matrix A:")
print(a)

transpose_a = np.transpose(a)

print("Transpose of Matrix A:")
print(transpose_a)


# ==============================
# Matrix Addition & Subtraction
# ==============================
A = np.array([[5, 8], [2, 6]])
B = np.array([[4, 7], [3, 9]])

matrix_sum = np.add(A, B)
matrix_diff = np.subtract(A, B)

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Sum:\n", matrix_sum)
print("Difference:\n", matrix_diff)


# ==============================
# Matrix Multiplication
# ==============================
# Scalar Multiplication
X = 5

M1 = np.random.randint(1, 10, size=(4, 4))

print("Scalar Value:", X)
print("Matrix 1:\n", M1)

product_scalar_matrix = np.multiply(X, M1)

print("Scalar * Matrix:\n", product_scalar_matrix)


# Element-wise Multiplication
M2 = np.random.randint(1, 10, size=(4, 4))

print("Matrix 2:\n", M2)

print("Element-wise Multiplication:\n", np.multiply(M1, M2))


# Matrix Multiplication (Dot Product)
print("Matrix Multiplication:\n", np.dot(M1, M2))
# Alternative: np.matmul(M1, M2)


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
