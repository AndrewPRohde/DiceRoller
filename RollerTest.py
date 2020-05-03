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
dice_dict = {'d2': 0, 'd4': 0, 'd6': 0, 'd8': 0, 'd10': 0, 'd12': 0, 'd20': 0, 'd100': 0}
for key in dice_dict:
    dice_dict[key] = tk.Radiobutton(frame, text=key, bd=4, width=10)
    dice_dict[key].config(indicatoron=0, variable=size, value=key)
    dice_dict[key].pack(side=LEFT)

# d2 = Radiobutton(window, text='d2', variable=size, value='d2').pack(anchor=W)
# d4 = Radiobutton(window, text='d4', variable=size, value='d4').pack(anchor=W)
# d6 = Radiobutton(window, text='d6', variable=size, value='d6').pack(anchor=W)
# d8 = Radiobutton(window, text='d8', variable=size, value='d8').pack(anchor=W)
# d10 = Radiobutton(window, text='d10', variable=size, value='d10').pack(anchor=W)
# d12 = Radiobutton(window, text='d12', variable=size, value='d12').pack(anchor=W)
# 20 = Radiobutton(window, text='d20', variable=size, value='d20').pack(anchor=W)
# d100 = Radiobutton(window, text='d100', variable=size, value='d100').pack(anchor=W)
quantity = Scale(window, from_=1, to=20, orient=HORIZONTAL).pack()
modifier = Scale(window, from_=-20, to=20, orient=HORIZONTAL).pack()
roll = tk.Button(window, text='Roll', width=25).pack(side=LEFT)
close = tk.Button(window, text='Close', width=25, command=window.destroy).pack(side=RIGHT)
window.mainloop()

dice = input("Please enter dice size: ")
quantity = input("Quantity: ")


# Logic for determining dice rolls
def rolldice(dice):
    result = 0
    if dice == "d2":
        result = diceSize.rolld2()
    elif dice == "d4":
        result = diceSize.rolld4()
    elif dice == "d6":
        result = diceSize.rolld6()
    elif dice == "d8":
        result = diceSize.rolld8()
    elif dice == "d10":
        result = diceSize.rolld10()
    elif dice == "d12":
        result = diceSize.rolld12()
    elif dice == "d20":
        result = diceSize.rolld20()
    elif dice == "d100":
        result = diceSize.rolld100()
    else:
        print("Please enter standard die")
    return result


while float(quantity) > 0:
    results = []
    rolled = rolldice(dice)
    results.append(rolled)
    quantity = float(quantity) - 1
    if dice == "d20":
        if rolled == 1:
            print("You rolled " + str(results) + " Critical Fail!")
        elif rolled == 20:
            print("You rolled " + str(results) + " Critical Success!")
        else:
            print("You rolled " + str(results))
    else:
        print("You rolled " + str(results))
