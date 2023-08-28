from turtle import Turtle
from random import choice, randrange, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def spawn(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            self.car = Turtle("square")
            self.car.penup()
            self.car.shapesize(1, 2)
            self.car.color(choice(COLORS))
            self.car.goto(260, randrange(-200, 250, 30))
            self.car.setheading(180)
            self.cars.append(self.car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_end(self):
        for car in self.cars:
            car.reset()
        self.speed += MOVE_INCREMENT
        self.cars.clear()
        