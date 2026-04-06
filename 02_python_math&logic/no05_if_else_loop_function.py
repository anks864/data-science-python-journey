"""
File: no05_if_else_loop_function.py
Topic: Conditional Statements, Loops, and Functions
Description: Covers if-else, loops, and a factorial function.
"""

# ==============================
# 1. If-Else
# ==============================
num1 = int(input("Enter value of A: "))
num2 = int(input("Enter value of B: "))

if num1 > num2:
    print("A is greater than B")
else:
    print("B is greater than or equal to A")


# ==============================
# 2. If-Elif-Else (Greatest Number)
# ==============================
num3 = int(input("Enter value of C: "))

if num1 > num2 and num1 > num3:
    print("A is the greatest number")
elif num2 > num3:
    print("B is the greatest number")
else:
    print("C is the greatest number")


# ==============================
# 3. Nested If
# ==============================
if num1 > num2:
    if num1 > num3:
        print("A is the greatest (nested)")
    else:
        print("C is the greatest (nested)")
else:
    if num2 > num3:
        print("B is the greatest (nested)")
    else:
        print("C is the greatest (nested)")


# ==============================
# 4. For Loop
# ==============================
num_laptops = int(input("Enter number of laptops: "))

total_price = 0
for i in range(num_laptops):
    price = int(input(f"Enter price of laptop {i + 1}: "))
    total_price += price

print("Total price:", total_price)


# ==============================
# 5. While Loop
# ==============================
number = int(input("Enter a number: "))

temp = number  # preserve original
while temp > 0:
    if temp % 2 == 0:
        print(temp, "is even")
    else:
        print(temp, "is odd")
    temp //= 2


# ==============================
# 6. Function (Factorial)
# ==============================
def factorial(n):
    if n < 0:
        return "Invalid Number"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


print("\nFACTORIAL")
user_number = int(input("Enter a number: "))
fact_value = factorial(user_number)
print(f"{user_number}! = {fact_value}")


# ==============================
# EOF: Feel free to open an issue for bugs or suggestions
# ==============================
