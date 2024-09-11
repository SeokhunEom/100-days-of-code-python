import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = 'https://www.zillow.com/ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-138.3349693125%2C%22east%22%3A-104.32129743750001%2C%22south%22%3A19.452009723387217%2C%22north%22%3A48.08976501506573%7D%2C%22mapZoom%22%3A5%2C%22usersSearchTerm%22%3A%22CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A9%2C%22regionType%22%3A2%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A648156%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8"
}
FORM_URL = "https://forms.gle/94ZaPaarXFAAxkbJ6"

response = requests.get(ZILLOW_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

houses = soup.select("li.ListItem-c11n-8-102-0__sc-13rwu5a-0")
house_info = []
for house in houses:
    try:
        price = house.select_one("span[data-test='property-card-price']").getText().split("+")[0].split("/")[0]
        address = house.select_one("address").getText()
        link = house.select_one("a").get('href')
        house_info.append({
            "price": price,
            "address": address,
            "link": link
        })
        if link.startswith("/"):
            link = f"https://www.zillow.com{link}"

    except AttributeError:
        pass


driver = webdriver.Chrome()

for house in house_info:
    driver.get(FORM_URL)
    time.sleep(3)

    price = house["price"]
    address = house["address"]
    link = house["link"]

    inputs = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd')
    inputs[0].send_keys(price)
    inputs[1].send_keys(address)
    inputs[2].send_keys(link)

    submit_button = driver.find_element(By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac')
    submit_button.click()
    time.sleep(1)

driver.quit()