import json
import os
import tkinter as tk
from tkinter import messagebox

# JSON file path
DATA_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

# Add a new task
def add_task():
    task_text = task_entry.get()
    if task_text.strip():
        tasks.append({"description": task_text, "completed": False})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Update task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{index+1}. {task['description']} {status}")

# Mark a task as completed
def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete!")

# Delete a selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create Tkinter GUI
root = tk.Tk()
root.title("Task Manager")

# Task entry field and button
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task list display
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Buttons for completing and deleting tasks
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Load tasks and update list
tasks = load_tasks()
update_task_list()

# Run Tkinter main loop
root.mainloop()
