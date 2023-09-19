import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def add():
    task = enter.get()
    if task:
        listbox.insert(tk.END, task)
        enter.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter your task.")

def delete():
    try:
        selected_task = listbox.curselection()[0]
        text = listbox.get(selected_task)
        if text == "Surfing":
            confirmed = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{text}'?")
            if confirmed:
                listbox.delete(selected_task)
        else:
            listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select your task to delete.")

def update():
    try:
        selected_task = listbox.curselection()[0]
        updated_task = enter.get()
        if updated_task:
            listbox.delete(selected_task)
            listbox.insert(selected_task, updated_task)
            enter.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def complete():
    try:
        selected_task = listbox.curselection()[0]
        listbox.itemconfig(selected_task, {'bg': '#008000'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select your task to mark as completed.")

# creating main application
root = tk.Tk()
root.title("To-Do List")
root.geometry("700x500")
root.configure(bg="#E0E0E0")
cfont = tkfont.Font(family="Comic Sans Ms", size=12)

enter = tk.Entry(root, width=30, font=cfont)
enter.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=20, height=2, command=add, bg="#4CAF50", fg="#FFFFFF", font=cfont)
add_button.grid(row=1, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Task", width=20, height=2, command=update, bg="#FF9800", fg="#FFFFFF", font=cfont)
update_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=20, height=2, command=delete, bg="#F44336", fg="#FFFFFF", font=cfont)
delete_button.grid(row=3, column=0, padx=10, pady=10)

complete_button = tk.Button(root, text="Mark as Completed", width=20, height=2, command=complete, bg="#2196F3", fg="#FFFFFF", font=cfont)
complete_button.grid(row=4, column=0, padx=10, pady=10)

listbox = tk.Listbox(root, width=34, height=18, font=cfont)
listbox.grid(row=1, column=1, rowspan=10, padx=10, pady=10)

root.mainloop()
