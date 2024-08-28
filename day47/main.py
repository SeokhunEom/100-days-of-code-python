import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.naver.com"
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

url = "https://www.amazon.com/dp/B0CCX11JT6?ref=dlx_deals_dg_dcl_B0CCX11JT6_dt_sl14_07&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price_whole = soup.select_one("span.a-price-whole").getText().replace(".", "")
price_fraction = soup.select_one("span.a-price-fraction").getText()
price = float(f"{price_whole}.{price_fraction}")
product_title = soup.select_one("span#productTitle").getText().strip()

if price < 350:
    msg = MIMEText(f"{product_title} is now {price}")
    msg['Subject'] ="Buy Now!"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg.as_string()
        )
