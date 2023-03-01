from turtle import Turtle
import random
from rgb import Rgb

rgb = Rgb()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Manager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_instance = random.randint(0,5)
        if random_instance == 5:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(rgb.rgb())
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed) #5

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

