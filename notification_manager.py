from twilio.rest import Client
import smtplib

TWILIO_SID = "AC02522b440347cf9624fe636d2ab7aa06"
TWILIO_AUTH_TOKEN= "6569870475b2d0a3e19263e3f789cdee"
TWILIO_VIRTUAl_NUMBER= "+16075368982"
TWILIO_VERIFIED_NUMBER= "+13144983524"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "abtestabtest123@gmail.com"
MY_PASSWORD = "Vini#2002"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        # message = self.client.messages.create(
        #     body=message,
        #     from_=TWILIO_VIRTUAl_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER,
        # )
        print(message)
        # Prints if successfully sent.
        # print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )