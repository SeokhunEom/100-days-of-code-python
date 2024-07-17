from turtle import Turtle, Screen

tim = Turtle()
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
