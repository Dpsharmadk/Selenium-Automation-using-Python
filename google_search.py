from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium Tutorial")

time.sleep(2)

search_box.submit()

time.sleep(3)

driver.refresh()

time.sleep(2)

driver.quit()