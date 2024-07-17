from turtle import Turtle, Screen
import random

colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan']
angle = [0, 90, 180, 270]

tim = Turtle()
tim.pensize(10)
tim.speed('fastest')

for i in range(1000):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()
