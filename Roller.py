import numpy as np
import array
import diceSize
import PySimpleGUI as gui

global rolled
#Gui build
gui.ChangeLookAndFeel('DarkPurple4')
layout = [[gui.Text('Dice to roll')], [gui.Radio('d2', "DICE"),gui.Radio('d4', "DICE"),gui.Radio('d6', "DICE"),gui.Radio('d8', "DICE"),gui.Radio('d10', "DICE"),gui.Radio('d12', "DICE"),gui.Radio('d20', "DICE", default=True),gui.Radio('d100', "DICE")], [gui.Text('Quantity'), gui.InputText('1')],[gui.Text('Modifier'), gui.Slider(range=(-20, 20), orientation='h', size=(34, 20), default_value=0)],[gui.Button('Roll'), gui.Exit()]]

window = gui.Window('Dice Roller', layout)

while True:
    event, values = window.read()
    print((event, values))


    if event in (None, 'Exit'):
        break
window.close()

text_input = rolled
gui.popup('You rolled ', text_input)

#button, (diceType) = form.Layout(layout).Read()


#quantity = input("How many? ")
#diceType = input("Which size dice? ")
if event(0):
    result = diceSize.rolld4()
    print(result)
if rolled == "d4":
    result = diceSize.rolld4()
    print(str(result))
elif rolled == "d6":
    result = diceSize.rolld6()
    print(str(result))
elif rolled == "d8":
    result = diceSize.rolld8()
    print(str(result))
elif rolled == "d10":
    result = diceSize.rolld10()
    print(str(result))
elif rolled == "d12":
    result = diceSize.rolld12()
    print(str(result))
elif rolled == "d20":
    result = diceSize.rolld20()
    if result == 1:
        print(str(result) + " Critical Fail!")
    elif result == 20:
        print(str(result) + " Critical Success!")
    else:
        print(str(result))
elif rolled == "d100":
    result = diceSize.rolld100()
    print(str(result))
else:
    print("Please enter standard dice size.")
    #diceType = input("Which size dice? ")
print(result)