from turtle import Turtle
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake :
    def __init__(self, length, start_position, point_size) :
        self.point_size = point_size
        self.segments = []
        for i in range(length):
            self.add_segment((start_position[0] - i * point_size, start_position[1]))
        self.head = self.segments[0]

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
    
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def collide_with_wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        return x > 290 or x < -290 or y > 290 or y < -290
    
    def collide_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True 
        return False
    
    def check_food_refresh(self, food):
        for segment in self.segments :
            if segment.distance(food) < 40:
                return False
        return True

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        
        self.__init__(3, (0, 0), 20)