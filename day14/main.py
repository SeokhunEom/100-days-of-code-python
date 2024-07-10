import random
import os
from art import logo, vs
from game_data import data


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_data():
    return random.choice(data)


def print_screen(data_a, data_b, score):
    cls()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data_a['name']}, {data_a['description']}, from {data_a['country']}")
    print(vs)
    print(f"Against B: {data_b['name']}, {data_b['description']}, from {data_b['country']}")
    return input("Who has more followers? Type 'A' or 'B': ").upper()


def play_round(data_a, score):
    data_b = get_random_data()
    while data_a == data_b:
        data_b = get_random_data()

    if data_a['follower_count'] >= data_b['follower_count']:
        answer = 'A'
    else:
        answer = 'B'

    user_choice = print_screen(data_a, data_b, score)
    if user_choice == answer:
        play_round(data_b, score + 1)
    else:
        end_game(score)


def end_game(score):
    cls()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


def play_game():
    data_a = get_random_data()
    play_round(data_a, 0)


play_game()
