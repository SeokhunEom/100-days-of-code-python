from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name.send_keys("FIRST")
last_name.send_keys("LAST")
email.send_keys("example@gmail.com")
button.click()

driver.quit()