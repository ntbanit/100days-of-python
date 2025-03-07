from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")   
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0)) 
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True   
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    
    # Detect collision with paddle
    if right_paddle.distance(ball) < 50 and ball.xcor() > 320 or left_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        # print(f"Right paddle distance: {right_paddle.distance(ball)} ycor: {right_paddle.ycor()}")
        # print(f"Left paddle distance: {left_paddle.distance(ball)} ycor: {left_paddle.ycor()}")
        # print(f"Ball ycor: {ball.ycor()}")
    
    # Reset ball bouncing state, to fix the bug ball is bouncing multiple times
    if right_paddle.distance(ball) < 50 and ball.xcor() < 320 or left_paddle.distance(ball) < 50 and ball.xcor() > -320:
        ball.reset_bouncing_state()

    # Detect if left paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position(-1)
        scoreboard.update_score("right")
    # Detect if right paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position(1)
        scoreboard.update_score("left")

screen.exitonclick()