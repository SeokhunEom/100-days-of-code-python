from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")

events = {}

for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text
    }
print(events)

driver.quit()