import tkinter as tk
from tkinter import simpledialog, messagebox


def word_sorter():
    try:
        # Get the number of words from the user
        word_number = simpledialog.askinteger("Word Count", "How many words do you have?")
        if word_number is None:
            return

        word_list = []
        for i in range(word_number):
            word = simpledialog.askstring("Word Input", f"Enter word {i + 1}:")
            if word:
                word_list.append(word)

        # Convert words to lowercase
        lower_words = [item.lower() for item in word_list]

        # Sort words alphabetically
        sorted_words = sorted(lower_words)

        # Display results
        result = "\n".join(f"{idx + 1}. word = {word}" for idx, word in enumerate(sorted_words))
        messagebox.showinfo("Sorted Words", result)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Main Tkinter window
def main():
    root = tk.Tk()
    root.title("Word Sorter")
    root.geometry("300x150")

    label = tk.Label(root, text="Word Sorting Program", font=("Arial", 14))
    label.pack(pady=10)

    sort_button = tk.Button(root, text="Start", command=word_sorter, font=("Arial", 12))
    sort_button.pack(pady=10)

    quit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12))
    quit_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
