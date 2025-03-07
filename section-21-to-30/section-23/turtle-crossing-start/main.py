import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen() 
screen.onkeypress(player.up, "Up")

game_is_on = True
cnt = 0
while game_is_on:
    time.sleep(0.1)
    cnt += 1
    screen.update()
    
    car_manager.move()
    if cnt % 7 == 0:
        car_manager.create_car()   
        cnt = 0
    
    # Detect player passing the finish line
    if player.is_at_finish_line():
        car_manager.increase_level()
        scoreboard.increase_level()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            screen.onkeypress(None, "Up")
screen.exitonclick()