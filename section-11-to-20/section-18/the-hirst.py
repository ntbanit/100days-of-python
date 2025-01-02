import colorgram

colors = colorgram.extract('image.jpg', 256)
rgb_list = []
for color in colors:
    c = color.rgb
    rgb = (c.r, c.g, c.b)
    rgb_list.append(rgb)

import random
import turtle

t = turtle.Turtle()

"""
draw 10 x 10 spots 
each dot size 20, space 50
"""
turtle.colormode(255)
t.penup()
# t.setposition(-200, -300)
t.setheading(225)
t.forward(300)
t.setheading(0)
t.pendown()
t.speed("fastest")
# color_idx = 0
radius = 20
space = 50
for i in range(10):
    cur_pos = t.position()
    for j in range(10):
        color = random.choice(rgb_list)
        # color_idx = (color_idx + 1) % len(rgb_list)

        # t.pencolor(color)
        # t.fillcolor(color)
        # t.begin_fill()
        # t.circle(radius)
        # t.end_fill()
        t.pendown()
        t.dot(radius, color)
        t.penup()

        t.forward(space)
    t.penup()
    t.setposition(cur_pos[0], cur_pos[1] + 50)


screen = turtle.Screen()
# screen.setup(width=1000, height=1500)
screen.exitonclick()