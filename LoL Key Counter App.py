import pynput
import sys
import PySimpleGUI as sg
from pynput.keyboard import Key, Listener

#LoL Key counter GUI
#Author: Briggs Clarke 

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('LoL Key Counter V1.0')],
            [sg.Text('Enter Key to be counted'), sg.InputText()],
            [sg.Button('Count'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()