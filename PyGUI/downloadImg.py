import requests
import bs4 as bs
import urllib.request
import os


# Class name = n3VNCb

# The URL
url = "https://www.google.com/search?q=cats&tbm=isch&ved=2ahUKEwj64NX3rcvqAhUOcqwKHX-HCV4Q2-cCegQIABAA&oq=cats&gs_lcp=CgNpbWcQA1AAWABgqrMPaABwAHgAgAEAiAEAkgEAmAEAqgELZ3dzLXdpei1pbWc&sclient=img&ei=I-sMX7rDOo7ksQX_jqbwBQ&bih=1297&biw=2560#imgrc=IMm8fKz2KPQZtM"

opener = urllib.request.build_opener()
opener.add_headers = [{"User-Agent": "Chrome"}]
urllib.request.install_opener(opener)

# Get the raw URL and make it a text
raw = requests.get(url).text

# Parse to scrape
soup = bs.BeautifulSoup(raw, "html.parser")
print(soup)
# Find all the image tag
# Put them in a list imgs
imgs = soup.findAll("img", {"class": "n3VNCb"})

print(imgs)
# Get all the images links
linksList = []
#
# for img in imgs:
#     # We want the src that stores the image
#     link = img.get('src')
#     # if the image does not have http
#     if 'http://' not in link:
#         link = url + link
#     linksList.append(link)

# Make a directory to store images
print(f'Images Dected: {len(linksList)}')
print(linksList)
yes = int(input("1 for yes, 0 for no: "))
if yes == 1:
    dirName = input("Enter Folder Name: ")
    os.mkdir(dirName)
    os.chdir(dirName)
    # How many images in the webpages
    for i in range(len(linksList)):
        fileName = f'img{i}.png'
        urllib.request.urlretrieve(linksList[i], fileName)
    print("Done!")