from datetime import datetime

sunrise_time = datetime.strptime('2025-03-24T05:00:00', '%Y-%m-%dT%H:%M:%S')
sunset_time = datetime.strptime('2025-03-24T17:00:00', '%Y-%m-%dT%H:%M:%S')
time_now = datetime.now()

if sunrise_time <= time_now <= sunset_time:
    currently_dark = True
else:
    currently_dark = False

print(currently_dark)