from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "purple", "green", "blue", "orange", "yellow", "indigo"]
racing_turtles = []
y_start = -120
for color in colors:
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.goto(-230, y_start)
    y_start += 40
    racer.color(color)
    racing_turtles.append(racer)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race ? Enter a color: (red, purple, green, blue, orange, yellow or indigo) :")
import random
result = ""
while result == "":
    for racer in racing_turtles:
        distance = random.randint(1, 10)
        racer.forward(distance)
        if racer.xcor() > 230:
            result = racer.pencolor()
            break
alert_text = f"You lost! Your guess is {user_bet} but the winner is {result}"
if user_bet == result:
    alert_text = f"You won! Turtle winner is {result}"

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Result", alert_text)
screen.exitonclick()