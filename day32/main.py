##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import glob
import random
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"


def make_letter(receiver_name):
    grob = glob.glob("letter_templates/*.txt")
    template = random.choice(grob)
    with open(template, "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", receiver_name)
        return letter


def make_email_msg(name, sender_email, receiver_email):
    letter = make_letter(name)
    msg = MIMEText(letter)
    msg['Subject'] ="Happy Birthday"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    return msg


def send_email(receiver_email, msg):
    with smtplib.SMTP("smtp.naver.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_email, msg=msg.as_string())


with open('birthdays.csv', "r") as file:
    birthdays = file.readlines()
    for data in birthdays[1:]:
        data = data.split(",")
        now = dt.datetime.now()
        month = now.month
        day = now.day
        if int(data[3]) == month and int(data[4]) == day:
            name = data[0]
            receiver_email = data[1]
            letter = make_email_msg(name, MY_EMAIL, receiver_email)
            send_email(receiver_email, letter)
