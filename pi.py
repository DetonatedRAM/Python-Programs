"""
Daniel Flores
8/8/2023

This program approximates the value of pi and then prints it above the true value of pi 
according to the math library. 
"""
import math
#After doing some research, this is one of the simpilist ways to calculate pi. (Leibniz formula) 
def calculate_pi_approximation(num_terms):
    approximation = 0
    for i in range(num_terms):
        term = (-1) ** i / (2 * i + 1)
        approximation += term

    return 4 * approximation

num_terms = 1000000
approximated_pi = calculate_pi_approximation(num_terms)

print("Approximation of π:", approximated_pi)
print("Value of π from math module:", math.pi)