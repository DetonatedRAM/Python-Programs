#Daniel Flores
#7/21/23

#This program will take a name as an input, then greets then using the name they entered if they enter my name or my professor's name. 

print("Please enter your name: ")
name = input()
if (name == "Daniel" or name == "Robyn"):
    print("Hello, " + name + "!")
else:
    print("Invalid Entry. Try again.")
