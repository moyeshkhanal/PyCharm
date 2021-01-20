import PySimpleGUI as sg

sg.theme_previewer()
layout = [[sg.Text(f"Name"), sg.Text("Age"), sg.Text("Grade")],
          [sg.Input(), sg.Input(), sg.Input()],
          [sg.Button("Add"), sg.Button("Exit")]]

window = sg.Window("First Window", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    print(event, value)

window.close()
