#Anoushka Saha
#Etch-A-Sketch
#Day 19 Project 1
#May 19th, 2024

#REQUIREMENTS
#W = forwards
#S = backwards
#A = counter-clockwise
#D = clockwise
#C = clear drawing

from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()

def w_forward():
    draw.forward(10)

def s_back():
    draw.backward(10)

def a_counter_clock():
    draw.left(10)

def d_clock():
    draw.right(10)

def c_clear():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()

screen.listen()
screen.onkey(key = "w", fun = w_forward)
screen.onkey(key = "s", fun = s_back)
screen.onkey(key = "a", fun = a_counter_clock)
screen.onkey(key = "d", fun = d_clock)
screen.onkey(key = "c", fun = c_clear)
screen.exitonclick()

