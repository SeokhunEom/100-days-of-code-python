import random
import smtplib
import datetime as dt
from email.mime.text import MIMEText

MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"
RECV_EMAIL = "recv_email@naver.com"


def get_quote():
    with open('quotes.txt', "r") as file:
        data = file.readlines()
        quote = random.choice(data)
        return quote


def make_msg():
    quote = get_quote()
    msg = MIMEText(quote)
    msg['Subject'] ="Today's Quote"
    msg['From'] = MY_EMAIL
    msg['To'] = RECV_EMAIL
    return msg


def send_email():
    msg = make_msg()
    with smtplib.SMTP("smtp.naver.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECV_EMAIL, msg=msg.as_string())


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    send_email()
