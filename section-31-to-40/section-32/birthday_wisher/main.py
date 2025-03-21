##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import pandas
birth_date_df = pandas.read_csv("birthdays.csv")
birth_date_dict = birth_date_df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
today = dt.date.today()

birthday_gang = []
for person in birth_date_dict:
    if today.month == person['month'] and today.day == person['day']:
        birthday_gang.append(person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# NEVER COMMIT THIS FOR SECURITY PROBLEM
my_email = ''
my_password = ''
# NEVER COMMIT THIS FOR SECURITY PROBLEM
import smtplib 
def send_birthday_email(person, file_letter_template):
    print(f"debug person: {person}")
    print(f"debug file_letter_template: {file_letter_template}")
    with open(file_letter_template, "r") as file:
        letter_template = file.read()
        letter_template = letter_template.replace("[NAME]", person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=person['email'], msg=f"Subject: Happy Birthday {person['name']}\n\n{letter_template}")

# 4. Send the letter generated in step 3 to that person's email address.
# list all files in the directory `letter_templates`
import os
import random
letter_templates = [file for file in os.listdir("letter_templates")]

for person in birthday_gang:
    letter_template = random.choice(letter_templates)
    send_birthday_email(person, f"letter_templates/{letter_template}")



