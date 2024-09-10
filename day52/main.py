from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
INSTA_USERNAME = os.getenv("INSTA_USERNAME")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(INSTA_USERNAME)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(INSTA_PASSWORD)
        time.sleep(3)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(5)

        followers_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, '팔로우')
        followers_button.click()
        time.sleep(5)

        for i in range(100):
            followers_list = self.driver.find_element(By.CSS_SELECTOR, 'div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(2)

    def follow(self):
        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button div._ap3a._aaco._aacw._aad6._aade')
        for button in all_follow_buttons:
            if button.text != '팔로우':
                continue
            button.click()
            time.sleep(2)

    def quit(self):
        time.sleep(10)
        self.driver.quit()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
