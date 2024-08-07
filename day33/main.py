import requests
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

MY_LAT = 37.566536
MY_LNG = 126.977966
MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"


#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        'tzid': 'Asia/Seoul'
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now()

    return sunset <= now.hour <= sunrise


def make_email_msg():
    msg = MIMEText(f'Look up! The ISS is nearby! Latitude: {iss_latitude}, Longitude: {iss_longitude}')
    msg['Subject'] ="Look up!"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    return msg


def send_email():
    with smtplib.SMTP("smtp.naver.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        msg = make_email_msg()
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.as_string())


while True:
    if is_iss_nearby() and is_night():
        send_email()
        break
    time.sleep(60)
