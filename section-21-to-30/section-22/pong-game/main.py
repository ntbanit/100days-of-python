from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")   
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0)) 
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True   
while game_is_on:
    screen.update()
    time.sleep(0.09)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()
    if right_paddle.distance(ball) < 30 or left_paddle.distance(ball) < 30:
        ball.bounce_paddle()

screen.exitonclick()