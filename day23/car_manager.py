from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        random_color = random.choice(COLORS)
        random_position = (300, random.randint(-240, 240))

        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random_color)
        new_car.goto(random_position)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)
                car.hideturtle()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

