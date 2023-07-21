# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is
#Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you
#return home after 10 nights you would return home on a Saturday (day 6) Write a general
#version of the program which asks for the starting day number, and the length of your stay, and
#it will tell you the number of day of the week you will return on.

#Daniel Flores
#7/21/2023

#This program asks what day you are leaving vacation, and then outputs the day you will return. The days are represented by numbers, 0 being Sunday, and 6 being Saturday.

print("Please enter the starting day number (0 for Sunday, 1 for Monday, 2 for Tuesday, etc.)")
startday = int(input())
print("Please enter how many days you will stay: ")
days_stayed = int(input())
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
returnday_index = (startday + days_stayed) % 7
returnday = days[returnday_index]
print("You will return on " + returnday)