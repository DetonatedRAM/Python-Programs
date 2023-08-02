#Daniel Flores
#8/1/2023

#This program creates a custom shape. 

import turtle
def draw(num_sides):
    t = turtle.Turtle()
    t.color("blue")
    for i in range(num_sides):
        t.forward(100)
        t.left(360/num_sides)
for _ in range (2,11):
    draw(_)