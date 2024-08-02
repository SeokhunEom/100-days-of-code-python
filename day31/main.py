import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

french_words_to_learn = df.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(cart_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(cart_word, text=current_card["English"], fill="white")


def on_wrong_button_click():
    next_card()


def on_right_button_click():
    french_words_to_learn.remove(current_card)
    data = pd.DataFrame(french_words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
cart_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=on_wrong_button_click)
wrong_button.grid(column=0, row=1)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0, command=on_right_button_click)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
