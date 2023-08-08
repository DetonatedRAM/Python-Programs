"""
Daniel Flores
8/8/2023

This program takes an input in radians and converts it to degrees. It then prints that value, as well
as the built-in conversion function from the math library. 
"""
import math

def calculate_pi_approximation(num_terms):
    approximation = 0
    for i in range(num_terms):
        term = (-1) ** i / (2 * i + 1)
        approximation += term

    return 4 * approximation

num_terms = 1000000
approximated_pi = calculate_pi_approximation(num_terms)

def radians_to_degrees(radians):
    return radians * (180 / approximated_pi)

input_radians = float(input("Enter a value in radians to convert to degrees: "))
my_degrees = radians_to_degrees(input_radians)
math_degrees = math.degrees(input_radians)

print("Calculated value in degrees: ", my_degrees)
print("Math module value in degrees: ", math_degrees)