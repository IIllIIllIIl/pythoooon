from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome()
driver.get("https://www.google.co.kr/?hl=ko")
driver.implicitly_wait(0.5)
query_text = "프로그래밍"
searchbox = driver.find_element(by=By.CSS_SELECTOR, value=".gLFyf")
searchbox.send_keys(query_text)
search_button = driver.find_element(by=By.CSS_SELECTOR, value=".gNO89b")
search_button.click()
temp_div = driver.find_element(by=By.CSS_SELECTOR, value=".hgKElc")
print("20317 송민재")
print(temp_div.text)
time.sleep(10)