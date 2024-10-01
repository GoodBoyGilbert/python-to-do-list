import tkinter as tk
from tkinter import messagebox

def addtask():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
  try:
    selected_task_index = listbox_tasks.curselection()[0]
    listbox_tasks.delete(selected_task_index)
  except:
    messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

window = tk.Tk()
window.title("To-Do List")

entry_task = tk.Entry(window, width=30)
entry_task.pack(pady=10)

listbox_tasks = tk.Listbox(window, height=10, width=45)
listbox_tasks.pack(pady=10)

btn_add_task = tk.Button(window, text="Add Task", width=15, command=addtask)
btn_add_task.pack(pady=5)

btn_delete_task = tk.Button(window, text="Delete Task", width=15, command=delete_task)
btn_delete_task.pack(pady=5)

btn_clear_tasks = tk.Button(window, text="Clear All Tasks", width=15, command=clear_tasks)
btn_clear_tasks.pack(pady=5)

window.mainloop()
