# from replit import clear
#HINT: You can call clear() to clear the output in the console.

import os
from art import logo


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


print(logo)
print("Welcome to the secret auction program.")

dict_bids = {}
max_bid = 0
max_bidder = ""

while True:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    dict_bids[name] = bid

    has_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if has_more_bidders == 'no':
        break

    cls()

for bidder in dict_bids:
    if dict_bids[bidder] > max_bid:
        max_bid = dict_bids[bidder]
        max_bidder = bidder

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
