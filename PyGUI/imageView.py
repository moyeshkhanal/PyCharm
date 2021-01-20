import PySimpleGUI as sg
# To get the image File Path
import os

# Image picker on the left
leftColumn = [
    [sg.Text("Image Folder"), sg.Input(size=(25,1), enable_events=True, key="FOLDER"), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="FILE LIST")]

]

# Image Column on the right
imageColumn = [
    [sg.Text("Select an image to view from the list on the left: ")],
    [sg.Text(size=(40,1), key="TEXTOUT")],
    [sg.Image(key="IMAGE")]
]

# This is the window layout
layout = [
    [
        sg.Column(leftColumn),
        sg.VerticalSeparator(),
        sg.Column(imageColumn)
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "FOLDER":
        # Get the folder path from the key FOLDER
        folder = values["FOLDER"]
        try:
            fileList = os.listdir(folder)
        except:
            fileList = []
        
        fileNames = [
            f for f in fileList
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png", ".gif"))
        ]
            
        window["FILE LIST"].update(fileNames)

    elif event == "FILE LIST":
        try:
            filePathName = os.path.join(values["FOLDER"], values["FILE LIST"][0])
            window["TEXTOUT"].update(filePathName)
            window["IMAGE"].update(filename=filePathName)
        except:
            pass

window.close()