from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FAKEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
tinder_url = "http://www.tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url=tinder_url)
time.sleep(2)

link_btn_loc= '//*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
login_linkButton = chrome_driver.find_element(By.XPATH, value=link_btn_loc)
login_linkButton.click()
time.sleep(2)

login_via = chrome_driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]')
login_w_Facebook = login_via.find_element(By.TAG_NAME, value='button')
login_w_Facebook.click()
time.sleep(2)

base_window = chrome_driver.window_handles[0]
fb_login_window = chrome_driver.window_handles[1]
chrome_driver.switch_to.window(fb_login_window)

email = chrome_driver.find_element(By.XPATH, value='//[@id="email"]')
password = chrome_driver.find_element(By.XPATH, value='//[@id="pass"]')
email.send_keys(FACEBOOK_EMAIL)
password.send_keys(FAKEBOOK_PASSWORD)
login_btn = chrome_driver.find_element(By.XPATH, value='//*[@id="loginbutton"]')
login_btn.click()
time.sleep(2)

chrome_driver.switch_to.window(base_window)
time.sleep(5)

loc_button = '//*[@id="q1656340203"]/main/div[1]/div/div/div[3]/button[1]'
allow_location_button = chrome_driver.find_element(By.XPATH, value=loc_button)
allow_location_button.click()
time.sleep(2)

btn_location='//*[@id="q1656340203"]/main/div[1]/div/div/div[3]/button[2]'
notifications_button = chrome_driver.find_element(By.XPATH, value=btn_location)
notifications_button.click()
time.sleep(2)

cookie_btn = '//*[@id="q1434999767"]/div/div[2]/div/div/div[1]/div[1]/button'
cookies = chrome_driver.find_element(By.XPATH, value=cookie_btn)
cookies.click()
time.sleep(2)

for skank_whore in range(100):
    time.sleep(3)

    try:
        dislike_button_path = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        dislike_button = chrome_driver.find_element(By.XPATH, value=dislike_button_path)
        dislike_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = chrome_driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(1)

chrome_driver.quit()