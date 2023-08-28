import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Road")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
i=0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.spawn()
    car_manager.move_car()

    if player.finish_level():
        scoreboard.score_track()
        player.spawn_turtle()
        car_manager.level_end()

    for car in car_manager.cars:
        if player.player.distance(car.position()) < 20:
            scoreboard.defeat()
            game_is_on = False
    screen.update()

screen.exitonclick()
