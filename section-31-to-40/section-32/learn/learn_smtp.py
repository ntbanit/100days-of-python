import smtplib 
# NEVER COMMIT THIS FOR SECURITY PROBLEM
my_email = ''
my_password = ''
my_client_email = ''
# NEVER COMMIT THIS FOR SECURITY PROBLEM
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_client_email, msg="Subject: Test Email\n\nThis is a test email.")
    connection.close()