import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()
    #detect collision with car
    for car in car_manager.list_cars:
        if (player.distance(car) < 20):
            scoreboard.game_over()
            game_is_on = False

    #detect successful crossing
    if (player.is_at_finish_line()):
        scoreboard.increment_level()
        car_manager.increase_speed()
        player.next_level()


screen.exitonclick()
