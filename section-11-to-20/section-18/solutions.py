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
def reset_random_color():
    global color_list
    color_list = []
    turtle.colormode(255)

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
    reset_random_color()
    for edge_cnt in range(3, 11):
        random_color()
        angle = 360 / edge_cnt
        for i in range(edge_cnt):
            timmy.forward(100)
            timmy.right(angle)

# video 133: self code
"""
1. random movements North, East, South, West
same distance (color) but it can at any point choose 
which direction it wants to go out of the four
eg: distance 3 : red - up left up, blue down down right ...
2. thickness the line 
3. speed up the turtle to draw much faster 
"""
def random_walk(distance, limit):
    timmy.pensize(10)
    timmy.speed("fastest")
    random_direction = [0, 90, 180, 270]
    reset_random_color()
    for i in range(limit):
        random_color()
        for j in range(distance):
            timmy.forward(30)
            timmy.right(random.choice(random_direction))

"""
video 135 : 
draw a number of circles with a radius of 100 in distance 
(r = 100) -> C = 2 * pi * r
in same 
"""
def draw_spirograph(moving):
    timmy.speed("fastest")
    reset_random_color()
    radius = 100
    start = 0
    while start < 360 :
        random_color()
        timmy.circle(radius)
        timmy.right(moving)
        start += moving
