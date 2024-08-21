import smtplib
from email.mime.text import MIMEText
import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.naver.com"
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def make_email_msg(self, message):
        msg = MIMEText(message)
        msg['Subject'] ="New Low Price Flight!"
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        return msg

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                msg = MIMEText(message)
                msg['Subject'] ="New Low Price Flight!"
                msg['From'] = MY_EMAIL
                msg['To'] = email

                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=msg.as_string()
                )
