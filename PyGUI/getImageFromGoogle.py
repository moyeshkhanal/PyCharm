import requests
import bs4 as bs
import urllib.request
import os

# Class name = n3VNCb

search = input("Enter search term: ")

# The URL
url = f"https://www.google.com/search?q={search}&sxsrf=ALeKk00yCaCYMA5I1WiNF-PLE6bX78hU7A:1594938179937&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi7kJ3d59LqAhXSXc0KHW53AHAQ_AUoAXoECB4QAw&biw=2560&bih=1297"

opener = urllib.request.build_opener()
opener.add_headers = [{"User-Agent": "Chrome"}]
urllib.request.install_opener(opener)

# Get the raw URL and make it a text
raw = requests.get(url).text

# Parse to scrape
soup = bs.BeautifulSoup(raw, "html.parser")
# print(soup.prettify())

# Find all the image tag
# Put them in a list imgs
# t0fcAb
imgs = soup.find_all("img", {"class": "t0fcAb"}, limit=10)
print(imgs)
# Get all the images links
linksList = []
#
for img in imgs:
    # We want the src that stores the image
    link = img.get('src')
    linksList.append(link)

# Make a directory to store images
print(f'Images Dected: {len(linksList)}')

yes = int(input("1 for yes, 0 for no: "))

if yes == 1:
    if not os.path.exists(search):
        os.mkdir(search)
    os.chdir(search)

    for i, links in enumerate(linksList):
        response = requests.get(links)
        imageName = os.getcwd() + "\\" + search + f"{i+1}" + ".jpg"
        with open(imageName, "wb") as file:
            file.write(response.content)

    print("Done!")