import PySimpleGUI as sg

# Default settings for buttons
# White Buttons
# 7 Characters long
# 2 Characters wide
bw = {"size": (7, 2), "font": ("Franklin Gothic Book", 24), "button_color": ("black", "#F8F8F8")}
# Tan Buttons
bt = {"size": (7, 2), "font": ("Franklin Gothic Book", 24), "button_color": ("black", "#F1EABC")}
# Orange Buttons
bo = {"size": (15, 2), "font": ("Franklin Gothic Book", 24), "button_color": ("black", "#ECA527"), "focus":True}

# Set the layout of the window
layout = [
    [sg.Text("Calculator", size=(50,1), justification="right", background_color="#272533", text_color="white")],
    [sg.Text("0.000", size=(18,1), justification="right", background_color="black", text_color="red")],
    [sg.Button("C", **bt), sg.Button("CE", **bt), sg.Button("%", **bt), sg.Button("/", **bt), ],
    [sg.Button("7", **bw), sg.Button("8", **bw), sg.Button("9", **bw), sg.Button("*", **bt), ],
    [sg.Button("4", **bw), sg.Button("5", **bw), sg.Button("6", **bw), sg.Button("-", **bt), ],
    [sg.Button("1", **bw), sg.Button("2", **bw), sg.Button("3", **bw), sg.Button("+", **bt), ],
    [sg.Button("0", **bw), sg.Button(".", **bw), sg.Button("=", **bo), ],
]

window = sg.Window("Calculator", layout=layout, background_color= "#272533", size=(580,660))

def numClicked(event):
    global decimal

    # if decimal:



def clear(event):
    pass

def displayUpdate(update):
    pass

def operatorClick(event):
    pass

while True:
    global decimal, result
    event, values = window.read()
    if event in "Exit" or event == sg.WIN_CLOSED:
        break
    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        numClicked(event)
    if event in ["C", "CE"]:
        clear(event)
        displayUpdate(0.0)
        # var["result"] = 0.0
    if event in ["+", "-", "*", "/"]:
        operatorClick(event)
    if event == "=":
        # equal()
        pass
    if event == ".":
        pass
        # var['decimal'] = True
    if event == "%":
        displayUpdate(result / 100.0)
    # Folder name was filled in, make a list of files in the folder
window.close()