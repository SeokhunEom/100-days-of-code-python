import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
                     [random.choice(symbols) for _ in range(random.randint(2, 4))] +
                     [random.choice(numbers) for _ in range(random.randint(2, 4))])
    random.shuffle(password_list)
    random_password = "".join(password_list)

    input_password.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_add():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                          f"Password: {password} \nIs it ok to save?")
    if not is_ok:
        return

    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

    input_website.delete(0, tk.END)
    input_password.delete(0, tk.END)
    input_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = tk.Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3)

input_website = tk.Entry(width=38)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = tk.Entry(width=38)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "tommya98@naver.com")

input_password = tk.Entry(width=21)
input_password.grid(column=1, row=3)

button_password = tk.Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3)

button_add = tk.Button(text="Add", width=36, command=on_add)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
