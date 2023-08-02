#Daniel Flores
#8/1/2023

#This program asks the user for the number of sides, the length of the side, the color of the sides, and the color that will fill in the shape. The program will then draw the described shape. 

import turtle
def draw(num_sides, side_length, line_color, fill_color):
    t = turtle.Turtle()
    t.color(line_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range(num_sides):   
        t.forward(side_length)
        t.left(360 / num_sides)
    t.end_fill()
    turtle.mainloop()
def main():
    num_sides = int(input("Enter the number of sides: "))
    side_length = int(input("Enter the length of the side: "))
    line_color = input("Enter the color of the line: ")
    fill_color = input("Enter the fill color: ")
    draw(num_sides, side_length, line_color, fill_color)

main()