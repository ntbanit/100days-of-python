STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE) 

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(0, -280)
            return True
        return False