from selenium import webdriver
from tkinter import Tk
import time

def main():
    tk = Tk()
    bot = webdriver.Chrome()
    bot.get("https://temp-mail.org/en/")
    time.sleep(3)
    bot.find_element_by_id("click-to-copy")
    text = tk.clipboard_get()
    bot.find_element_by_id("click-to-delete")
    emails = []
    passwords = ["123456", "7891234"]
    for i in range(2):
        em = bot.find_element_by_id("click-to-copy")
        time.sleep(2)
        em.click()
        time.sleep(2)
        text = tk.clipboard_get()
        emails.append(text)
        delt = bot.find_element_by_id("click-to-delete")
        time.sleep(2)
        delt.click()
        time.sleep(5)
    print(emails)

main()