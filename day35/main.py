import requests
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "API_KEY"

parameters = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": API_KEY
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
today_whether_data = weather_data["list"][:8]

will_rain = False
for hour_data in today_whether_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

with smtplib.SMTP("smtp.naver.com") as connection:
    if will_rain:
        msg = MIMEText('Bring an umbrella today.')
    else:
        msg = MIMEText('No rain today.')
    msg['Subject'] = "Today's Weather"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.as_string())
