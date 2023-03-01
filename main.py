from turtle import Turtle, Screen
import time
from player import Player
from car_manager import Manager
from scoreboard import Scoreboard

screen  = Screen()
screen.colormode(255)
screen.setup(600, 600)
screen.tracer(0)
player = Player()
manegar = Manager()
score = Scoreboard()


game_on = True
while game_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkeypress(player.move,"Up")

    manegar.move_car()

    # if player.ycor() > 280:
    #     player.finish()

    for car in manegar.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.on_finish_line():
        player.home_pos()
        manegar.level_up()
        score.level_update()

    screen.update()
    manegar.create_car()

screen.exitonclick()
