from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome = webdriver.Chrome()
chrome.get("https://www.google.com")
inputBar = chrome.find_element_by_name("q")

chrome.manage().windows().getSize()
inputBar.send_keys("cute cats")
inputBar.send_keys(Keys.RETURN)

fst = chrome.find_element_by_partial_link_text("pin").click()

scroll = 0
while scroll < 2500:
    chrome.execute_script(f"window.scrollTo(0, {scroll});")
    scroll += 100
