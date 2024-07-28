COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.list_cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        rand_chance = random.randint(1, 4)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randrange(-250, 250, 20)
            new_car.goto(300, new_y)
            self.list_cars.append(new_car)

    def move_car(self):
        for car in self.list_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
