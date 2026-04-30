"""
File: no06_numerical_python.py
Topic: NumPy (Numerical Python)
Description: Demonstrates NumPy operations, array creation, performance comparison, and manipulation.
"""


# ==============================
# Importing Libraries
# ==============================
import numpy as np
from time import process_time


# ==============================
# 1. Performance Comparison (List vs NumPy)
# ==============================
python_list = [i for i in range(1000000)]

start_time_list = process_time()
python_list = [i + 5 for i in python_list]
end_time_list = process_time()

print("Time taken by Python list:", end_time_list - start_time_list)

np_array = np.array([i for i in range(1000000)])

start_time_np = process_time()
np_array += 5
end_time_np = process_time()

print("Time taken by NumPy array:", end_time_np - start_time_np)


# ==============================
# 2. Creating NumPy Arrays
# ==============================
one_d_array = np.array([1, 2, 3, 4, 5])
print(one_d_array, type(one_d_array), "Shape:", one_d_array.shape)

two_d_array = np.array([(1, 2, 3), (4, 5, 6)], dtype=float)
print(two_d_array, type(two_d_array), "Shape:", two_d_array.shape)


# ==============================
# 3. Initializing Arrays
# ==============================
zeros_array = np.zeros((3, 5))
print("Zeros:\n", zeros_array)

ones_array = np.ones((4, 7), dtype=int)
print("Ones:\n", ones_array)

full_array = np.full((2, 6), 8.23)
print("Full:\n", full_array)

identity_matrix = np.eye(4)
print("Identity Matrix:\n", identity_matrix)

random_array = np.random.random((4, 5))
print("Random (0-1):\n", random_array)

random_int_array = np.random.randint(30, 70, (3, 6))
print("Random Integers:\n", random_int_array)

linspace_array = np.linspace(10, 30, 6, dtype=int)
print("Linspace:\n", linspace_array)

arange_array = np.arange(10, 30, 5.5)
print("Arange:\n", arange_array)


# ==============================
# 4. List to NumPy Array
# ==============================
sample_list = [10, 20, 30, 40, 50, 60]
numpy_array = np.asarray(sample_list)
print(numpy_array, type(numpy_array))


# ==============================
# 5. Analyzing NumPy Array
# ==============================
random_matrix = np.random.randint(10, 90, (4, 7))

print("Array:\n", random_matrix)
print("Shape:", random_matrix.shape)
print("Dimensions:", random_matrix.ndim)
print("Number of elements:", random_matrix.size)
print("Data type:", random_matrix.dtype)


# ==============================
# 6. Mathematical Operations
# ==============================
list1 = [9, 8, 7, 6, 5]
list2 = [1, 2, 3, 4, 5]
print("List concatenation:", list1 + list2)

array1 = np.random.randint(11, 20, (3, 3))
array2 = np.random.randint(1, 10, (3, 3))

print("Array 1:\n", array1)
print("Array 2:\n", array2)

print("Sum:\n", np.add(array1, array2))
print("Difference:\n", np.subtract(array1, array2))
print("Product:\n", np.multiply(array1, array2))
print("Quotient:\n", np.divide(array1, array2))
print("Remainder:\n", np.remainder(array1, array2))


# ==============================
# 7. Array Manipulation
# ==============================
matrix = np.random.randint(11, 20, (2, 3))
print("Original Matrix:\n", matrix, matrix.shape)

transpose_matrix = matrix.T
print("Transpose:\n", transpose_matrix, transpose_matrix.shape)

reshaped_matrix = matrix.reshape(3, 2)
print("Reshaped Matrix:\n", reshaped_matrix, reshaped_matrix.shape)


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
