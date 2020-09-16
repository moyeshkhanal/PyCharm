from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox = webdriver.Chrome()
firefox.get(r'https://www.reddit.com/r/wildlifephotography/')
response = BeautifulSoup(firefox.page_source, features='lxml')
image_divs = response.find('div',
                           attrs={'class': 'rpBJOHq2PR60pnwJlUyP0'})
image_tags = image_divs.find_all('img')
for i in image_tags:
    print(i['src'])  # Various interesting methods to extract image!
# JavaScriptExecutor - for visualization of scrolling
    i.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for i in image_tags:
    print(i['src'])