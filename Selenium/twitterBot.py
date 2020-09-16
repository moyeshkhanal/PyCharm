from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):

        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(2)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(1)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/hashtag/"+ hashtag +"?src=hashtag_click")
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_element_by_class_name("css-1dbjc4n")
            links = [elem.get_attribute("data-permalink-path") for elem in tweets]
            print(links)

    def tweet(self):
        bot = self.bot
        bot.get("https://twitter.com/compose/tweet")
        compose = bot.find_element_by_class_name("DraftEditor-root").send_keys("Hello World")
        time.sleep(15)

def main():
    ed = TwitterBot('twitterbot@netmail8.com', 'TwitterBot')
    ed.login()
    ed.like_tweet("python")
    # ed.tweet()

if __name__ == '__main__':
    main()