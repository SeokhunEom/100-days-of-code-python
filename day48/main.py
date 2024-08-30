from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 60*5
timeout2 = time.time() + 5
while True:
    cookie.click()
    if time.time() > timeout2:
        store = driver.find_elements(By.CSS_SELECTOR, '#store b')
        store.reverse()
        store = store[1:]
        for item in store:
            item.click()
        timeout2 = time.time() + 5

    if time.time() > timeout:
        click_per_sec = driver.find_element(By.ID, 'cps')
        print(click_per_sec.text)
        break

driver.quit()