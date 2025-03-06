from turtle import Turtle
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake :
    def __init__(self, length, start_position, point_size) :
        self.point_size = point_size
        self.segments = []
        self.current_direction = "right"
        self.create_snake(length, start_position, point_size)

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
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    