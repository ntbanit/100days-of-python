from turtle import Turtle
import random

class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("green")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        x_random = random.randint(-260, 260)
        y_random = random.randint(-260, 260)
        self.goto(x_random, y_random)