"""
File: no01_python_basics.py
Topic: Python Basics
Description: printing, data types, variables, and user input.
"""

# ==============================
# 1. Basic Printing
# ==============================
print("Hello")

# Joining text and adding numbers
print("AI & ML" + " Projects")  # '+' concatenates strings
print("AI & ML", "Projects")    # ',' adds space between values
print(8 + 3)                   # addition


# ==============================
# 2. Basic Data Types
# ==============================
print(type(8))        # int
print(type(34.56))    # float
print(type("String")) # str


# ==============================
# 3. Variables and Assignment
# ==============================
super_hero = "Iron Man"
print(super_hero)

super_hero = "Captain America"  # reassignment
print(super_hero)

hero1, hero2, hero3 = "Iron Man", "Wonder Woman", "Spider Man"
print(hero1, hero2)  # prints with space separation
print(hero3)


# ==============================
# 4. Multiple Variables Same Value
# ==============================
x = y = z = 23
print(x, y, z)
print(id(x), id(y), id(z))  # same memory reference


# ==============================
# 5. User Input and Typecasting
# ==============================
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("Concatenation:", num1 + num2)           # string concatenation
print("Addition:", int(num1) + int(num2))     # typecasting to int


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
