from turtle import Turtle, Screen
import random

colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan']
angle = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
tim.speed('fastest')
screen = Screen()
screen.colormode(255)

gap = 5
for _ in range(int(360 / gap)):
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.setheading(tim.heading() + gap)

screen.exitonclick()
