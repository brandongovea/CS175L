#CS 175L
#Brandon Govea
#STOP

import math
import turtle

#Names constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

#Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

#Calculate the diameter of the octagon so we can center it in the graphics window.
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

#initialize the turtle
turtle.speed(ANIMATION_SPEED)
turtle.pendown()
turtle.color("white", "red")
turtle.pensize(LENGTH // 10)
turtle.begin_fill()

#Draw the octagon
for x in range(NUM_SIDES):
    turtle.forward(100)
    turtle.right(ANGLE)
turtle.end_fill()

turtle.color("red")
turtle.penup()
turtle.goto(-7, 11)
turtle.pendown()
turtle.begin_fill
for x in range(NUM_SIDES):
    turtle.forward(110)
    turtle.right(ANGLE)
turtle.end_fill
    
#Display 'Stop'
turtle.penup()
turtle.goto(-25,-150)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", font = ("Arial", 60))
turtle.hideturtle()
