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
        user_name_elem = driver.find_element_by_name('username')
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_name('password')
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(2)

    def like_photo(self, user_id):
        driver = self.driver
        driver.get("https://www.instagram.com/" + user_id + "/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time(2)



myInstagramLogin = InstagramBot('', '')     # enter your username and password
myInstagramLogin.login()
myInstagramLogin.like_photo('jsbaidwan')
