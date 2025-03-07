COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE   

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 250))
        car.setheading(180)
        self.all_cars.append(car)
    
    def increase_level(self):
        self.move_distance += MOVE_INCREMENT
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.move_distance)
