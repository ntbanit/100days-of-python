import os
import smtplib
class NotificationManager:
    def __init__(self):
        self.notification_email = os.environ['MY_SEND_EMAIL']
        self.notification_password = os.environ['MY_SEND_EMAIL_PASSWORD']
        self.client_email = os.environ['MY_CLIENT_EMAIL']
    
    def send_email(self, flight_data):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.notification_email, password=self.notification_password)
            connection.sendmail(from_addr=self.notification_email
                                , to_addrs=self.client_email
                                , msg="Subject: Flight Deal Coder Aleart\n\n" \
                                f"From {flight_data.origin_city} to {flight_data.destination_city}.\n" \
                                f"Price: {flight_data.price} EUR.\n" \
                                f"Link: {flight_data.link}\n")