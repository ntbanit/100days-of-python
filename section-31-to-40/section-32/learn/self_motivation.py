import smtplib 

def send_motivation_email(motivation_quote):
    # NEVER COMMIT THIS FOR SECURITY PROBLEM
    my_email = ''
    my_password = ''
    my_client_email = ''
    # NEVER COMMIT THIS FOR SECURITY PROBLEM
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_client_email, msg=f"Subject: Self Motivation Quote\n\n{motivation_quote}")
        connection.close()

import datetime as dt
import random
current_time = dt.datetime.now()
if current_time.weekday() == 4:
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        motivation_quote = random.choice(lines).strip()
        print(f"Motivation Quote for the day: {motivation_quote}")
        send_motivation_email(motivation_quote)