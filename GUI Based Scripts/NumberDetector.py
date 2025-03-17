import tkinter as tk
from tkinter import messagebox, simpledialog


def number_detector():
    try:
        start = simpledialog.askinteger("Start Number", "Enter the first number of the range:")
        end = simpledialog.askinteger("End Number", "Enter the last number of the range:")
        step = simpledialog.askinteger("Step Number", "Enter the step size of the range:")

        if start is None or end is None or step is None:
            return  # Exit if the user cancels the input

        number_list = list(range(start, end, step))
        messagebox.showinfo("Number List", f"{number_list}")
        messagebox.showinfo("List Size", f"Total numbers: {len(number_list)}")

        even_list = [i for i in number_list if i % 2 == 0]
        odd_list = [i for i in number_list if i % 2 != 0]

        messagebox.showinfo("Even Numbers", ", ".join(map(str, even_list)))
        messagebox.showinfo("Odd Numbers", ", ".join(map(str, odd_list)))

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def main():
    root = tk.Tk()
    root.title("Number Detector App")
    root.geometry("300x150")

    label = tk.Label(root, text="Number Detector", font=("Arial", 14))
    label.pack(pady=10)

    start_button = tk.Button(root, text="Start", command=number_detector, font=("Arial", 12))
    start_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12))
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
