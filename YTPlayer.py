import PySimpleGUI as sg
import os.path
import webbrowser
import time

import PySimpleGUI as sg


def play(url, times):
    for i in range(0, times):
            webbrowser.open(url, new=1)
            time.sleep(20)

sg.theme('BluePurple')

layout = [[sg.Text('Paste URL', font='Any 18'), 
            sg.Text('                                      Enter No. of Times (<=10)', font='Any 18'), sg.Text(size=(30, 4), key='-OUTPUT-')],
          [sg.Input(key='-IN-'), sg.Input(key='-IN2-')],
          [sg.Button('Ok'), sg.Button('Exit')]]

window = sg.Window(title="YT Video Viewer (use wisely, don't misuse)", layout = layout, margins=(100, 50))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if(event == sg.WIN_CLOSED or event == 'Exit'):
        break
    if(event == 'Ok'):
        url = values['-IN-']
        times = min(10, int(values['-IN2-']))
        play(url, times)

window.close()
