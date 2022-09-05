import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path= "F:\\Python\Selenium-Python\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com")
print(driver.title)

driver.implicitly_wait(10)

driver.find_element(By.NAME, 'q').send_keys("kiama blowhole")

optionsList = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print (len(optionsList))

for ele  in optionsList:
    print(ele.text)

    if ele.text == 'kiama blowhole news':
        ele.click()
        break

time.sleep(5)
driver.quit()

def my_func():
    print('Hello world')
