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

        for i in range(1, 3):   # set the number of scroll required
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if user_id in href]
        print(user_id + ' photos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)


myInstagramLogin = InstagramBot('', '')     # enter your username and password
myInstagramLogin.login()
myInstagramLogin.like_photo('jsbaidwan')
