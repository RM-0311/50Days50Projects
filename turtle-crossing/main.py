import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Level()
level.update_level()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # Detect Player making it to top of screen
    if player.ycor() > 290:
        level.increase_level()
        player.reset()
        # car_count += 10

    # Generate Cars
    car = CarManager()

    
screen.exitonclick()