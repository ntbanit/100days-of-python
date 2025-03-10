from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        with open("data.txt") as file:
            self.high_point = int(file.read())  
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def increase_point(self):
        self.point += 1
        self.update_scoreboard()

    def update_scoreboard(self):  
        self.clear()
        self.write(f"Score: {self.point} High Score: {self.high_point}", align="center", font=("Consolas", 12, "normal"))
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("Game Over", align="center", font=("Consolas", 24, "normal"))

    def reset(self):
        if self.point > self.high_point:
            self.high_point = self.point
            with open("data.txt", "w") as file:
                file.write(str(self.high_point))
        self.point = 0
        self.update_scoreboard()