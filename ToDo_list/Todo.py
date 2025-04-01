import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List Application")

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append({"name": task, "completed": False})
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task!")

def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        listbox.insert(tk.END, f"{task['name']} - {status}")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()