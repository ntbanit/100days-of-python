import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(3, (0, 0), 20)
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
def reset_game():
    global game_is_on
    game_is_on = True
    food.refresh()
    scoreBoard.reset()
    snake.reset()
    game_loop()
screen.onkey(reset_game, "Return")

def game_loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.15)
        snake.move()

        if snake.head.distance(food) < 40:
            while not snake.check_food_refresh(food):
                food.refresh()
            scoreBoard.increase_point()
            snake.extend()
        
        if snake.collide_with_wall() or snake.collide_with_tail():
            game_is_on = False
game_loop()            
        
screen.exitonclick()
