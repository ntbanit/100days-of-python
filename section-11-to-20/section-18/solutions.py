import turtle
from turtle import Turtle, Screen

timmy = Turtle()

def draw_a_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)

# video 131: self code
def draw_a_dashed_line(length):
    for i in range(length):
        timmy.color("black")
        timmy.forward(10)
        timmy.color("white")
        timmy.forward(10)

# video 131: answer code
def solution_dashed_line():
    for i in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

import random

color_list = []
def random_color():
    global color_list
    while True:
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        rgb = f"{red} {blue} {green}"

        if rgb not in color_list:
            timmy.pencolor(red, green, blue)
            timmy.fillcolor(red, green, blue)
            color_list.append(rgb)
            break

# video 132: self code
def draw_complex():
    turtle.colormode(255)
    for edge_cnt in range(3, 11):
        random_color()
        angle = 360 / edge_cnt
        for i in range(edge_cnt):
            timmy.forward(100)
            timmy.right(angle)

# video 133: self code
def random_walk():
    # TODO: 1.
    pass