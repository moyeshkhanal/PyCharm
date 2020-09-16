import PySimpleGUI as sg
import os

sg.theme('Dark Brown')

btn = {"size": (7, 2), "font": ("Franklin Gothic Book", 18), "button_color": ("black", "#F8F8F8")}

layout = [[sg.Text("Hello"), sg.Button("Button", **btn)],
          [sg.Input("Hello", key="-Mo-"), sg.FolderBrowse()],
          [sg.In(), sg.Ok(), sg.Cancel()],
          [sg.In(), sg.FileBrowse()]]

window = sg.Window("First Window", layout)

event, values = window.read()
print(event, values)
if values['Browse'] != "":
    os.chdir(values['Browse'])
print(os.getcwd())

window.close()