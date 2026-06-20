from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.amazon.in")

time.sleep(2)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Headphones")

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

time.sleep(5)

products = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

print("Product Names:\n")

for product in products[:10]:
    print(product.text)

time.sleep(2)

driver.quit()