import tkinter as tk
from tkinter import ttk
import random

def winner(u_choice, cod_choice):
    if u_choice == cod_choice:
        return "It's a tie!"
    elif (
            (u_choice == "Rock" and cod_choice == "Scissor")
            or (u_choice == "Paper" and cod_choice == "Rock")
            or (u_choice == "Scissor" and cod_choice == "Paper")
    ):
        return "You win!"
    else:
        return "CodSoft wins!"

def play(choice):
    c_choices = ["Rock", "Paper", "Scissors"]
    cod_choice = random.choice(c_choices)

    result = winner(choice, cod_choice)
    res_label.config(text=f"You choose {choice}\nCodSoft choose {cod_choice}\n{result}")

game = tk.Tk()
game.title("Rock-Paper-Scissors Game")
game.geometry("500x350")

button_style = ttk.Style()
button_style.configure("TButton", font=("Helvetica", 12), padding=5, width=15)

label = ttk.Label(game, text="Choose :", font=("Helvetica", 14),foreground="#00008B")
label.pack(pady=10)

rock_b = ttk.Button(game, text="Rock", style="TButton", command=lambda: play("Rock"))
paper_b = ttk.Button(game, text="Paper", style="TButton", command=lambda: play("Paper"))
scissor_b = ttk.Button(game, text="Scissor", style="TButton", command=lambda: play("Scissor"))
rock_b.pack(pady=10)
paper_b.pack(pady=10)
scissor_b.pack(pady=10)

res_label = ttk.Label(game, text="", font=("Comic Sans Ms", 14), background="#3EB489")
res_label.pack(pady=10)

game.mainloop()
