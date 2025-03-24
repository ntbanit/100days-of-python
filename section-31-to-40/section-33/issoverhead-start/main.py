import requests
from datetime import datetime

MY_LAT = 21.027763 # Your latitude
MY_LONG = 105.834160 # Your longitude

def check_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    print(f"Current distance: LAT={abs(iss_latitude - MY_LAT)} LONG={abs(iss_longitude - MY_LONG)}")
    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def currently_dark():
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise_time = datetime.strptime(data['results']['sunrise'], '%Y-%m-%dT%H:%M:%S%z')
    sunset_time = datetime.strptime(data['results']['sunset'], '%Y-%m-%dT%H:%M:%S%z')
    time_now = datetime.now().astimezone()
    # print(sunrise_time)
    # print(sunset_time)
    # print(f"Time now: {time_now}")
    bright_time = sunrise_time <= time_now <= sunset_time
    print(f"Is bright time: {bright_time}")
    return not bright_time

# NEVER COMMIT THIS FOR SECURITY PROBLEM
my_email = ''
my_password = ''
my_client_email = ''
# NEVER COMMIT THIS FOR SECURITY PROBLEM
import smtplib
def send_email():   
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_client_email, msg="Subject: ISS Overhead Alert\n\nLook up!")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

currently_dark()
check_iss_overhead()
# import time
# while True:
#     if check_iss_overhead() and currently_dark():
#         send_email()
#     time.sleep(60)  # Check every 60 seconds
