import requests
parameters = {
    'lat': 13.399263,
    'lng': 108.439178,
    'tzid': 'Asia/Ho_Chi_Minh',
    'formatted': 0
}
response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

from datetime import datetime

sunrise_time = datetime.strptime(data['results']['sunrise'], '%Y-%m-%dT%H:%M:%S%z')
sunset_time = datetime.strptime(data['results']['sunset'], '%Y-%m-%dT%H:%M:%S%z')
print(sunrise_time)
print(f"Sunrise time: {sunrise_time.hour}:{sunrise_time.minute}:{sunrise_time.second}")
print(sunset_time)
print(f"Sunset time: {sunset_time.hour}:{sunset_time.minute}:{sunset_time.second}")