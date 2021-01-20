import PySimpleGUI as sg

leftColumn = [
    [sg.Text("Left Column", key="LTEXT")],
    [sg.In(key="IN")],
    [sg.Button("Press me", key="BTN")]
]

rightColumn = [
    [sg.Text("Right Column")]
]

layout = [
    [
        sg.Column(leftColumn),
        sg.VerticalSeparator(),
        sg.Column(rightColumn)
    ]
]

window = sg.Window("Test", layout, finalize=True, size=(500, 500))
# window.size(50, 50)
# window.maximize()
while True:
    event, values = window.read()
    print(event, values)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "BTN":
        window["LTEXT"].update(values["IN"])

window.close()