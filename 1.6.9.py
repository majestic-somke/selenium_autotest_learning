from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/registration1.html" # old registration1.html
link = "http://suninjuly.github.io/registration2.html" #new registration2.html


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first") # First name
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second") # Last name
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third") # Email
    input3.send_keys("ivan@petrov.com")

    # input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first") # Phone
    # input4.send_keys("1234567")
    #
    # input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second") # Address
    # input5.send_keys("Russia")


    button = browser.find_element(By.CLASS_NAME, "btn.btn-default") # Button
    button.click()

finally:
    time.sleep(5)
    browser.quit()

