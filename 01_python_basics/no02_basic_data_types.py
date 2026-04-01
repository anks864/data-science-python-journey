"""
File: no02_basic_data_types.py
Topic: Python Data Types
Description: numeric types, type conversion, boolean, and string operations.
"""

# ==============================
# 1. Integer
# ==============================
a = 8
print(a, "-", type(a))


# ==============================
# 2. Floating Point
# ==============================
b = 2.3
print(b, "-", type(b))


# ==============================
# 3. Complex Numbers
# ==============================
c = 1 + 3j  # 'j' represents imaginary part
print(c, "-", type(c))


# ==============================
# 4. Type Conversion
# ==============================
print(a, "-> float:", float(a), "-", type(float(a)))
print(b, "-> int:", int(b), "-", type(int(b)))
print(a, "-> complex:", complex(a), "-", type(complex(a)))
# Note: complex to int/float is not directly possible


# ==============================
# 5. Boolean
# ==============================
x, y = True, False
print(x, type(x), y, type(y))

comparison = 7 < 3
print("Is 7 < 3?", comparison, type(comparison))


# ==============================
# 6. Strings and Operations
# ==============================
print("Machine Learning:", "Learning it!")   # comma adds space
print("Machine Learning:" + "Learning it!") # '+' joins without space

text = "Courses"
print(text, type(text))
print(text * 5)  # repetition


# ==============================
# 7. String Slicing
# ==============================
strg = "for Machine Learning"
print(strg[1:15])     # substring
print(strg[0:15:2])   # step slicing
print(text + strg)    # concatenation


# ==============================
# 8. Mutability Concept
# ==============================
# Immutable types: int, float, string, bool, tuple

a = 5
print("a = 5 ->", id(a))

a = 7
print("a = 7 ->", id(a))

b = 5
print("b = 5 ->", id(b))

b = 7
print("b = 7 ->", id(b))

# Mutable types: list, set, dictionary


# ==============================
# 9. Mini Practice
# ==============================
num = float(input("Enter a number: "))
print("Integer:", int(num))
print("Float:", float(num))
print("Complex:", complex(num))

# ==============================
