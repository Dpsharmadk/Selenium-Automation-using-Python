from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.amazon.in")

time.sleep(2)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptop")

time.sleep(2)

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

time.sleep(5)

driver.refresh()

time.sleep(2)

driver.quit()