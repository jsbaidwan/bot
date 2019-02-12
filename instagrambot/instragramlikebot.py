from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")


driver.find_element_by_name("q").send_keys("Jaspreet Singh Baidwan    ")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
