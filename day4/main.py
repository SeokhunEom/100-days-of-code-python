rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]
results = [[
    "It's a draw!",
    "You lose!",
    "You win!",
], [
    "You win!",
    "It's a draw!",
    "You lose!",
], [
    "You lose!",
    "You win!",
    "It's a draw!"
]]

print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    print("Computer chose:")
    print(game_images[computer_choice])

    print(results[user_choice][computer_choice])
