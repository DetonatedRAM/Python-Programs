#Daniel Flores
#7/21/23

#This program will compute the miles per gallon of a car. It asks for the miles driven, and the number of gallons used. 

print("Please enter miles driven: ")
miles = int(input())
print("Please enter gallons of gasoline used: ")
gallons = int(input())
mpg = miles/gallons
print("Your vehicles reaches " + str(mpg) + " miles per gallon. ")