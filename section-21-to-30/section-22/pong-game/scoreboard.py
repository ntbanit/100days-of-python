from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score(None)
    
    def update_score(self, winner):
        if winner == "left":
            self.l_score += 1
        elif winner == "right":
            self.r_score += 1
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Consolas", 30, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Consolas", 30, "normal"))