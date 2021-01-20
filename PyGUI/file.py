import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.ButtonMenu("Menu", menu_def=["menu", ["Two", "Three"]], key="btn-menu")],
            [sg.Radio("Checkbox", 2, key="check-box")],
            [sg.Checkbox('Another Checkbox', default=True, key="one"), sg.Checkbox('Another Checkbox2', default=True, key="two")],
            [sg.OK(), sg.Cancel(), sg.Submit()]]

window = sg.Window('Get filename example', layout)
while True:

    event, values = window.read()
    print(event, values)
    if event == "OK" or event is None:
        break

window.close()



layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()
#
# import os
#
#
# def make_file_python(ProjectName): #function to make python project
#     os.makedirs('../' + ProjectName)
#     open(f"..\{ProjectName}\start.py", 'x')
#
# def make_file_webapp(ProjectName): #function to make webapp project
#     os.makedirs('../' + ProjectName)
#     open(f"..\{ProjectName}\index.html", 'x')
#     open(f"..\{ProjectName}\style.css", 'x')
#     open(f"..\{ProjectName}\script.js", 'x')
#
# sg.change_look_and_feel('DarkAmber') #colour
#
# #layout of window
# layout = [
#     [sg.Text('File Types')],
#     [sg.Radio('Python file (start.py)', 1, key='-PY-')],
#     [sg.Radio('Web app (script.js, index.html, styles.css)', 1, key='-WEB-')],
#     [sg.Text('Project Name:'), sg.InputText(key='-NAME-')],
#     [sg.Button('Ok'), sg.Button('Cancel')],
# ]
# window = sg.Window('Project Creator', layout) #make the window
#
# while True:
#     event, values = window.read()
#     ProjectName = values['-NAME-']
#     if event in (None, 'Cancel'):
#         break
#     if values['-PY-'] and ProjectName:
#         make_file_python(ProjectName)
#         break
#     elif values['-WEB-'] and ProjectName:
#         make_file_webapp(ProjectName)
#         break
#
# window.close()

# import PySimpleGUI as sg

"""
    Multiple Window Design Pattern

    Two windows - both remain active and visible
    Window 1 launches Window 2
    Window 1 remains visible and active while Window 2 is active
    Closing Window 1 exits application

    Copyright 2020 PySimpleGUI.org
"""

#
# def make_window1():
#     layout = [[sg.Text('Window 1'), ],
#               [sg.Input(enable_events=True, k='-IN-')],
#               [sg.Text(size=(20, 1), k='-OUTPUT-')],
#               [sg.Button('Launch 2'), sg.Button('Exit')]]
#
#     return sg.Window('Window 1', layout, finalize=True)
#
#
# def make_window2():
#     layout = [[sg.Text('Window 2')],
#               [sg.Button('Exit')]]
#
#     return sg.Window('Window 2', layout, finalize=True)
#
#
# def main():
#     window1, window2 = make_window1(), None
#     while True:
#         window, event, values = sg.read_all_windows()
#         if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
#             break
#         # Window 1 stuff
#         if event == '-IN-':
#             window['-OUTPUT-'].update(values['-IN-'])
#         elif event == 'Launch 2' and not window2:
#             window2 = make_window2()
#
#         # Window 2 stuff
#         if window == window2 and event in (sg.WIN_CLOSED, 'Exit'):
#             window2.close()
#             window2 = None
#
#     window1.close()
#     if window2 is not None:
#         window2.close()
#
#
# if __name__ == '__main__':
#     main()