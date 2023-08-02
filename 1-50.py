#Daniel Flores
#8/1/2023

#This program itterates through the numbers 1-50, and prints the number. However, if the number being printed is divisible by 3 or 5 or both, the program will print that instead. 

def one_fifty():
    for num in range (1,51):
        if num % 3 == 0 and num % 5 == 0:
            print("Divisible by both")
        elif num % 3 == 0:
            print("Divisible by three")
        elif num % 5 == 0:
            print("Divisible by five")
        else:
            print(num)
one_fifty()