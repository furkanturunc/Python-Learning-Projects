from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1,2)
        car.color(random.choice(COLORS))
        car.penup()
        car.left(180)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def refresh(self):
        self.move()
        self.create_cars()

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def hits(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True

        return False

