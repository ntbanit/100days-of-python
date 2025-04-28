import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationManager:
    def __init__(self):
        self.notification_email = os.environ['MY_SEND_EMAIL']
        self.notification_password = os.environ['MY_SEND_EMAIL_PASSWORD']
    
    def send_email(self, client_email, mail_title, message_body):
        # Create a MIMEText email
        msg = MIMEMultipart()
        msg['From'] = self.notification_email
        msg['To'] = client_email
        msg['Subject'] = mail_title

        # Attach the message body with UTF-8 encoding
        msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

        # Send the email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.notification_email, password=self.notification_password)
            connection.sendmail(from_addr=self.notification_email,
                                to_addrs=client_email,
                                msg=msg.as_string())