import requests
import datetime
from newsapi import NewsApiClient
import smtplib
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "STOCK_API_KEY"
STOCK_API_URL = "https://www.alphavantage.co/query"

NEWS_API_KEY = "NEWS_API_KEY"

MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

def get_stock():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }

    response = requests.get(STOCK_API_URL, params=parameters)
    stock_data = response.json()

    date_diff = 1
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday_close_price = 0
    day_before_yesterday_close_price = 0

    while yesterday_close_price == 0:
        if date in stock_data["Time Series (Daily)"]:
            today_data = stock_data["Time Series (Daily)"][date]
            yesterday_close_price = float(today_data["4. close"])
        date = datetime.datetime.now() - datetime.timedelta(days=date_diff)
        date = date.strftime("%Y-%m-%d")
        date_diff += 1

    while day_before_yesterday_close_price == 0:
        if date in stock_data["Time Series (Daily)"]:
            today_data = stock_data["Time Series (Daily)"][date]
            day_before_yesterday_close_price = float(today_data["4. close"])
        date = datetime.datetime.now() - datetime.timedelta(days=date_diff)
        date = date.strftime("%Y-%m-%d")
        date_diff += 1

    price_diff = yesterday_close_price - day_before_yesterday_close_price
    percentage = (price_diff / day_before_yesterday_close_price) * 100
    return percentage


def get_news():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                          language='en',
                                          sort_by='publishedAt',
                                          page_size=3,
                                          page=1)
    articles = all_articles["articles"]
    return articles


def send_email(percentage, articles):
    with smtplib.SMTP("smtp.naver.com") as connection:
        text = ""
        for article in articles:
            text += f"Headline: {article['title']}.\nBrief: {article['description']}.\nURL: {article['url']}\n\n"

        msg = MIMEText(text)
        msg['Subject'] = f"{STOCK}: {'🔺' if percentage > 0 else '🔻'}{round(abs(percentage), 2)}%"
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL

        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.as_string())


def main():
    percentage = get_stock()
    if abs(percentage) > 5:
        articles = get_news()
        send_email(percentage, articles)
    else:
        print("No news to send.")


main()