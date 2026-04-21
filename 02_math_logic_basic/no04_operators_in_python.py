"""
File: no04_operators_in_python.py
Topic: Python Operators
Description: Covers arithmetic, assignment, comparison, logical, identity, and membership operators.
"""

# ==============================
# 1. Arithmetic Operators
# ==============================
num1 = 20
num2 = 15

print("num1 =", num1)
print("num2 =", num2)

print("Sum:", num1 + num2)             # addition
print("Difference:", num1 - num2)      # subtraction
print("Product:", num1 * num2)         # multiplication
print("Division:", num1 / num2)        # quotient
print("Floor Division:", num1 // num2) # floor value
print("Modulus:", num1 % num2)         # remainder
print("Exponent:", num1 ** num2)       # power


# ==============================
# 2. Assignment Operators
# ==============================
value = 8
print("Initial value:", value)

value += 5
print("After += 5:", value)

value -= 10
print("After -= 10:", value)

value *= 20
print("After *= 20:", value)

value /= 7
print("After /= 7:", value)

value //= 3
print("After //= 3:", value)

value %= 7
print("After %= 7:", value)

value **= 5
print("After **= 5:", value)


# ==============================
# 3. Comparison Operators
# ==============================
first_num = 3
second_num = 6

print("first_num =", first_num)
print("second_num =", second_num)

print("Equal:", first_num == second_num)
print("Not Equal:", first_num != second_num)
print("Greater Than:", first_num > second_num)
print("Greater Than or Equal:", first_num >= second_num)
print("Less Than:", first_num < second_num)
print("Less Than or Equal:", first_num <= second_num)


# ==============================
# 4. Logical Operators
# ==============================
print("AND:", first_num > 5 and first_num < 5)
print("OR:", first_num > 5 or first_num < 5)
print("NOT:", not (first_num > 5))


# ==============================
# 5. Identity Operators
# ==============================
x = 5
y = 5

print("x is y:", x is y)
print("x is not y:", x is not y)


# ==============================
# 6. Membership Operators
# ==============================
element = 10
number_list = [4, 8, 12, 16, 20]

print("List:", number_list)
print("Element in list:", element in number_list)
print("Element not in list:", element not in number_list)


# ==============================
# 7. Mini Practice
# ==============================
num = int(input("Enter a number: "))

if num % 2 == 0 and num >= 0:
    print("Positive Even Number")
elif num % 2 != 0 and num >= 0:
    print("Odd Number")
else:
    print("Negative Number")


# ==============================
# EOF: Feel free to open an issue for bugs or suggestions
# ==============================
