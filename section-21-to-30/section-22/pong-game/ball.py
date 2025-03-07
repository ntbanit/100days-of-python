from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = 5 
        self.bouncing = False
        self.move_speed = 1.2
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)      
            
    def reset_position(self, direction):
        self.goto(0, 0)
        self.x_move = 5 * direction
        self.y_move = 5 * direction
        self.reset_bouncing_state()

    def bounce_wall(self):
        self.y_move *= -1
        self.y_move *= self.move_speed
    
    def bounce_paddle(self):
        if not self.bouncing:
            self.x_move *= -1
            self.x_move *= self.move_speed
            self.bouncing = True
        
    def reset_bouncing_state(self):
        self.bouncing = False   