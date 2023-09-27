from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from calc import calc

link = "http://suninjuly.github.io/execute_script.html"


browser = webdriver.Chrome()
browser.get(link)

xx = browser.find_element(By.ID, "input_value").text
y = calc(xx)
# x = xx.get_attribute("valuex")


input_box = browser.find_element(By.ID, "answer")
input_box.send_keys(y)

time.sleep(1)
browser.execute_script("window.scrollBy(0, 100);")


option1 = browser.find_element(By.ID, "robotCheckbox") # СТАВИТ ГАЛКУ
option1.click()

option2 = browser.find_element(By.ID, "robotsRule") # RADIO # ВЫБИРАЕТ ИЗ ПРЕДЛОЖЕННЫХ ВАРИАНТОВ
option2.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()