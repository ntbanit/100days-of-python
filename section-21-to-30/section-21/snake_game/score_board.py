from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
    
    def update_score(self):
        self.point += 1      
        self.clear()
        self.write(f"Score: {self.point}", align="center", font=("Consolas", 12, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Consolas", 24, "normal"))