import tkinter as tk

def cal():
    num1 = int(enter1.get())
    num2 = int(enter2.get())

    if opr.get() == "+":
        result = num1 + num2
    elif opr.get() == "-":
        result = num1 - num2
    elif opr.get() == "*":
        result = num1 * num2
    elif opr.get() == "/":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2
    else:
        result = "Error: Invalid operation"

    res.delete(0, tk.END)
    res.insert(0, result)

# Creating the main window
root = tk.Tk()
root.title("CodSoft Calculator")
root.geometry("488x300")

enter1 = tk.Entry(root, width=16, font=("Arial", 16))
enter1.grid(row=0, column=0, padx=10, pady=10)

opr = tk.StringVar()
opr.set("+")  # set default operation
opr_dropdown = tk.OptionMenu(root, opr, "+", "-", "*", "/")
opr_dropdown.grid(row=0, column=1)

enter2 = tk.Entry(root, width=16, font=("Arial", 16))
enter2.grid(row=0, column=2, padx=10, pady=10)

res = tk.Entry(root, width=28)
res.grid(row=1, column=0, columnspan=3)

button = tk.Button(root, text="Calculate", command=cal, font=("Arial", 16))
button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
