from turtle import Turtle, Screen
import random

colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan']

tim = Turtle()
for i in range(3, 11):
    tim.color(random.choice(colors))
    angle = 360 / i
    for j in range(i):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
