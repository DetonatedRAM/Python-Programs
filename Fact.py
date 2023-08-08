"""
Daniel Flores
8/8/2023

This program calculates the factorial of a user input. It prints this value and then the calulated value
using the math 
"""
import math

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

user_input = int(input("Enter a non-negative integer: "))
calculated_factorial = calculate_factorial(user_input)
math_module_factorial = math.factorial(user_input)

print("Calculated factorial:", calculated_factorial)
print("Factorial using math module:", math_module_factorial)