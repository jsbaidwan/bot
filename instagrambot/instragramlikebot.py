from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        loginButton = driver.find_element_by_link_text('Log in')
        loginButton.click()
        loginButton.send_keys(Keys.ENTER)
        time.sleep(2)



myInstagramLogin = InstagramBot('fdkjgkdf', 'dfkjg')     # enter your username and password
myInstagramLogin.login()

