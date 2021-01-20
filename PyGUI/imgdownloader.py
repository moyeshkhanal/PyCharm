import requests
import bs4 as bs
import PySimpleGUI as sg
import urllib.request
from PIL import Image
import os

"""
Image Downloader by Croix Suhy

Created for the Congressional App Challenge
"""

# Sets the theme for the window
sg.theme("Dark Blue 3")

# Parts of the windows

# This is for the search bar and image list
imgSearcher = [
    [sg.Text("Enter your search query"), sg.Text("Number of images to download")],
    [sg.Input(key="SEARCH QUERY"), sg.Text(size=(15, 1))],
    [sg.Text("Min"), sg.Slider(range=(1, 20), default_value=20, orientation="h", key="IMAGE LIMIT"), sg.Text("Max")],
    [sg.Text(size=(2, 1))],
    [sg.Button(button_text="Submit", key="Submit"), sg.Button(button_text="Delete Selected Image", key="Delete Image"), sg.Button(button_text="Delete All Images (WIP)", key="Delete All")],
    [sg.Text(size=(5, 1))],
    [sg.Text("Select a image to preview")],
    [sg.Listbox(values=[], enable_events=True, size=(30, 10), key="IMAGE LIST")]
]

# This part is for the image viewer
imgViewer = [
    [sg.Text("Image Viewer")],
    [sg.Image(key="IMAGE")],
    [sg.Text(size=(40, 20))]
]

# Layout for the entire window
layout = [[sg.Column(imgSearcher), sg.VerticalSeparator(), sg.Column(imgViewer)]]

window = sg.Window("Image Downloader", layout)

# Fake browser (we are using Chrome), used for going to Google Images
opener = urllib.request.build_opener()
opener.add_headers = [{"User Agent": "Chrome"}]
urllib.request.install_opener(opener)

# List of files to be deleted, will be explained later in this code
dirsToBeDel = []

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Submit":
        """
        This section is for submitting images and downloading them.
        """

        searchQuery = values["SEARCH QUERY"]

        url = f"https://www.google.com/search?q={searchQuery}&sxsrf=ALeKk00yCaCYMA5I1WiNF-PLE6bX78hU7A:1594938179937&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi7kJ3d59LqAhXSXc0KHW53AHAQ_AUoAXoECB4QAw&biw=2560&bih=1297"

        # Gets the raw HTML data and gets text
        rawUrl = requests.get(url).text

        # BeautifulSoup parses the raw HTML data
        soup = bs.BeautifulSoup(rawUrl, "html.parser")

        imgLimit = int(values["IMAGE LIMIT"])

        # Gets image links with the class t0fcAb
        images = soup.find_all("img", {"class": "t0fcAb"}, limit=imgLimit)

        imgLinks = []

        # Gets all the links of the image and puts into a list
        for img in images:
            imgLink = img.get("src")
            imgLinks.append(imgLink)

        # Creates folder, if it exists, skip
        try:
            if not os.path.exists(searchQuery):
                os.mkdir(searchQuery)
            os.chdir(searchQuery)
        except:
           sg.Popup("Please type in a search query", title="Error")

        # Creates a blank .png file and gets image data from the list
        for i, links in enumerate(imgLinks):
            getLinks = requests.get(links)
            imgName = os.path.join(os.getcwd(), f"{searchQuery}{i + 1}.png")
            with open(imgName, "wb") as file:
                file.write(getLinks.content)

        # Creates a list of all images, if none exist, make it blank
        try:
            imageList = os.listdir(os.getcwd())
        except:
            imageList = []

        # Gives all images a path and checks to make sure it exists
        files = [
            i for i in imageList
            if os.path.isfile(os.path.join(os.getcwd(), i)) and i.lower().endswith(".png")
        ]

        currentDir = os.getcwd()

        os.chdir("../")

        # Updates the image list on the screen and clears input box
        window["IMAGE LIST"].update(files)
        window["SEARCH QUERY"].update("")

    if event == "Delete Image":
        """
        This section is for deleting images.
        """

        # Removes selected image from the list, if it doesn't exist, skip.
        try:
            os.remove(os.path.join(currentDir, values["IMAGE LIST"][0]))

            try:
                imageList = os.listdir(currentDir)
            except:
                imageList = []

            window["IMAGE LIST"].update(imageList)
        except:
            sg.Popup("Please select an image", title="Error")

    if event == "IMAGE LIST":
        """
        This section is for updating the image list on the screen.
        """

        # Shows image that's been clicked on the right side on the screen
        try:
            imgPath = os.path.join(currentDir, values["IMAGE LIST"][0])
            window["IMAGE"].update(filename=imgPath)
        except:
            # Not all pngs are equal, and some have left over jpeg data. To make it so we can view it,
            # we convert it into a png again, making it a true png file
            try:
                os.chdir(currentDir)
                with Image.open(values["IMAGE LIST"][0]) as badImage:
                    fixBadImage = badImage.convert("RGB")
                    fixBadImage.save(values["IMAGE LIST"][0])
                    imgPath = os.path.join(os.getcwd(), values["IMAGE LIST"][0])
                    window["IMAGE"].update(filename=imgPath)

            except:
                sg.Popup("No image selected", title="Error")

            os.chdir("../")

    if event == "Delete All":
        """
        This section is for deleting all images. (WORK IN PROGRESS)
        """
        try:
            for i in range(len(files)):
                delImgPath = os.path.join(currentDir, files[i])

                if os.path.exists(delImgPath):
                    os.remove(delImgPath)

            files = []
            imageList = []

            dirsToBeDel.append(currentDir)
            imageList = []
            window["IMAGE"].update(imageList)
            window["SEARCH QUERY"].update("")

        except:
            sg.Popup("Image file not found", title="Error")


# Closes window when program is terminated
window.close()

# Deletes directorys you dont want at the end
for dir in dirsToBeDel:
    os.rmdir(dir)