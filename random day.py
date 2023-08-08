"""
Daniel Flores
8/8/2023

This program selects and prints a random day from a list of days. 
"""
import random

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
random_day = random.choice(days)
print(random_day)