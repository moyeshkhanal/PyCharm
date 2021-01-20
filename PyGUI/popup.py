import PySimpleGUI as sg

layout = [[sg.Button("Hello")]
          ]


window = sg.Window("Image Viewer", layout)

event, values = window.read()

while True:
    print(event, values)
    if event == "Hello":
        sg.Popup('Ok clicked')
        print(event, values)
        break
window.close()