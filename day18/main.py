from turtle import Turtle, Screen
import random

#import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69),
              (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164),
              (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187),
              (169, 207, 170), (220, 181, 168)]


def random_color():
    return random.choice(color_list)


tim = Turtle()
tim.speed('fastest')
screen = Screen()
screen.colormode(255)

for y in range(10):
    for x in range(10):
        tim.penup()
        tim.goto(x * 50 - 250, y * 50 - 250)
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.dot(10, random_color())

screen = Screen()
screen.exitonclick()
