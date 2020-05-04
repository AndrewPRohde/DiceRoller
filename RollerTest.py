import tkinter

import diceSize
import numpy
import tkinter as tk
from tkinter import *

# GUI configuration
window = tk.Tk()
window.title('Dice Roller')
frame = Frame(window).pack()
dicesize = Label(window, text='Please choose dice size').pack()
size = tk.StringVar()
quant = tk.IntVar()
mod = tk.IntVar()


def roll_dice():
    print("Dice size is: ", size.get())
    choice = size.get()
    quantity_rolled = quant.get()
    modifier_added = mod.get()

    # Logic for determining dice rolls

    def rolldice(choice):
        result = 0
        if choice == "d2":
            result = diceSize.rolld2()
        elif choice == "d4":
            result = diceSize.rolld4()
        elif choice == "d6":
            result = diceSize.rolld6()
        elif choice == "d8":
            result = diceSize.rolld8()
        elif choice == "d10":
            result = diceSize.rolld10()
        elif choice == "d12":
            result = diceSize.rolld12()
        elif choice == "d20":
            result = diceSize.rolld20()
        elif choice == "d100":
            result = diceSize.rolld100()
        else:
            print("Please enter standard die")
        return result

    results = []
    while float(quantity_rolled) > 0:
        rolled = rolldice(choice)
        results.append(rolled)
        quantity_rolled = float(quantity_rolled) - 1
        if choice == "d20":
            if rolled == 1:
                print("You rolled " + str(results) + " Critical Fail!")
            elif rolled == 20:
                print("You rolled " + str(results) + " Critical Success!")

    window.update()
    print(results)

# Window containing roll results
    results_window = Toplevel()
    results_window.title("Roll Results")
    total = Message(results_window, text="You Rolled: " + str(results))
    total.pack()

    def add_modifier():
        if modifier_added != 0:
            total_roll = sum(results) + modifier_added
            print("This is the total of your roll: " + str(total_roll))
            return total_roll

    summed_roll = add_modifier()


def quit_loop():
    window.destroy()


dice_dict = {'d2': 0, 'd4': 0, 'd6': 0, 'd8': 0, 'd10': 0, 'd12': 0, 'd20': 0, 'd100': 0}
for key in dice_dict:
    dice_dict[key] = tk.Radiobutton(frame, text=key, bd=4, width=10)
    dice_dict[key].config(indicatoron=0, variable=size, value=key)
    dice_dict[key].pack(side=LEFT)

howmany = Scale(window, from_=1, to=20, orient=HORIZONTAL, label='Quantity', variable=quant).pack()
modifier = Scale(window, from_=-20, to=20, orient=HORIZONTAL,label='Modifier', variable=mod).pack()
roll = tk.Button(window, text='Roll', width=25, command=roll_dice).pack(side=LEFT)
close = tk.Button(window, text='Close', width=25, command=quit_loop).pack(side=RIGHT)
window.mainloop()
