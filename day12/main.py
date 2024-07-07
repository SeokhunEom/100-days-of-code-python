#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo
import random

print(logo)
print("Welcome to the number guessing game!")

print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    guess = 10
else:
    guess = 5

while guess > 0:
    print(f"You have {guess} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif user_guess > answer:
        print("Too high.")
    else:
        print("Too low.")
    guess -= 1

if guess == 0:
    print(f"You've run out of guesses, the answer was {answer}. You lose.")
