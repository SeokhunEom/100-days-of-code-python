import turtle
import pandas as pd

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
states = data['state'].to_list()

total_states = len(states)
correct = 0

while correct < total_states:
    user_input = screen.textinput(f"{correct}/{total_states} States Correct", "What's another state's name?").title()

    if user_input == "Exit":
        missing_states = pd.DataFrame(states)
        missing_states.to_csv("missing_states.csv")
        break

    if user_input in states:
        state_data = data[data['state'] == user_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(user_input)
        states.remove(user_input)
        correct += 1
