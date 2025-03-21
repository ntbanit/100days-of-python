from turtle import Turtle
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake :
    def __init__(self, length, start_position, point_size) :
        self.point_size = point_size
        self.segments = []
        self.create_snake(length, start_position, point_size)
        self.head = self.segments[0]

    def create_snake(self, length, start_position, point_size):
        for i in range(length):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(start_position[0] - i * point_size, start_position[1])
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(self.point_size)
        # self.segments[0].left(90)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    