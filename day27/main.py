import tkinter as tk

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)


def calculate():
    miles = float(user_input.get())
    km = miles * 1.609344
    label_result.config(text=f"{km:.2f}")


user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)

label_miles = tk.Label(text="Miles", font=("Arial", 24))
label_miles.grid(column=2, row=0)

label_equal = tk.Label(text="is equal to", font=("Arial", 24))
label_equal.grid(column=0, row=1)

label_result = tk.Label(text="0", font=("Arial", 24))
label_result.grid(column=1, row=1)

label_km = tk.Label(text="Km", font=("Arial", 24))
label_km.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
