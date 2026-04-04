"""
File: no02_basic_data_types.py
Topic: Python Data Types
Description: Covers numeric types, type conversion, boolean logic, and string operations.
"""

# ==============================
# 1. Integer
# ==============================
integer_num = 8
print(integer_num, "-", type(integer_num))


# ==============================
# 2. Floating Point
# ==============================
float_num = 2.3
print(float_num, "-", type(float_num))


# ==============================
# 3. Complex Numbers
# ==============================
complex_num = 1 + 3j  # 'j' represents imaginary part
print(complex_num, "-", type(complex_num))


# ==============================
# 4. Type Conversion
# ==============================
print(integer_num, "-> float:", float(integer_num), "-", type(float(integer_num)))
print(float_num, "-> int:", int(float_num), "-", type(int(float_num)))
print(integer_num, "-> complex:", complex(integer_num), "-", type(complex(integer_num)))
# Note: complex to int/float is not directly possible


# ==============================
# 5. Boolean
# ==============================
is_valid = True
is_complete = False
print(is_valid, type(is_valid), is_complete, type(is_complete))

comparison_result = 7 < 3
print("Is 7 < 3?", comparison_result, type(comparison_result))


# ==============================
# 6. Strings and Operations
# ==============================
course_text = "Machine Learning"
print(course_text + " is interesting!")   # concatenation
print(course_text, "Learning it!")        # comma adds space

word = "Courses"
print(word, type(word))
print(word * 5)  # repetition


# ==============================
# 7. String Slicing
# ==============================
sentence = "for Machine Learning"
print(sentence[1:15])     # substring
print(sentence[0:15:2])   # step slicing
print(word + sentence)    # concatenation


# ==============================
# 8. Mutability Concept
# ==============================
# Immutable types: int, float, string, bool, tuple

value = 5
print("value = 5 ->", id(value))

value = 7
print("value = 7 ->", id(value))

another_value = 5
print("another_value = 5 ->", id(another_value))

another_value = 7
print("another_value = 7 ->", id(another_value))

# Mutable types: list, set, dictionary


# ==============================
# 9. Mini Practice
# ==============================
user_number = float(input("Enter a number: "))

print("As Integer:", int(user_number))
print("As Float:", float(user_number))
print("As Complex:", complex(user_number))

# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
