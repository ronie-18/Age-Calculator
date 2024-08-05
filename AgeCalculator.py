import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def calculate_age():
    birthdate = entry.get()
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.today()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        messagebox.showinfo("Age Calculator", f"Your age is: {age}")
    except ValueError:
        messagebox.showerror(
            "Invalid Date", "Please enter the date in YYYY-MM-DD format"
        )


# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place the labels and entry widget
tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=20)

# Start the main event loop
root.mainloop()
