import tkinter as tk
from tkinter import StringVar, messagebox

# Basic arithmetic functions
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        return "Error: Division by zero!"
    return number1 / number2

# Get user input and validate operation
def get_input():
    try:
        operation = operation_var.get()
        number1 = float(entry1.get())
        number2 = float(entry2.get())

        if operation not in ["+", "-", "*", "/"]:
            messagebox.showerror("Error", "Invalid operation!")
            return None, None, None

        return operation, number1, number2

    except ValueError:
        messagebox.showerror("Error", "Invalid number input!")
        return None, None, None

# Perform calculation
def calculate():
    operation, number1, number2 = get_input()
    if operation is None:
        return

    if operation == "+":
        result = add(number1, number2)
    elif operation == "-":
        result = subtract(number1, number2)
    elif operation == "*":
        result = multiply(number1, number2)
    elif operation == "/":
        result = divide(number1, number2)
    else:
        result = "Error!"

    result_label.config(text=f"Result: {result}")

# Tkinter main window
root = tk.Tk()
root.title("Calculator")

# Input fields
tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation (+, -, *, /):").grid(row=2, column=0)
operation_var = StringVar()
operation_entry = tk.Entry(root, textvariable=operation_var)
operation_entry.grid(row=2, column=1)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Start Tkinter loop
root.mainloop()
