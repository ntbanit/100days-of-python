import requests
import os 
# Run in Microsoft Windows
# $env:MY_APPID = "MY_APPID"
HANOI_POSITION = (21.027763, 105.834160)
parameter = {
    'appid': os.environ.get('MY_APPID'),
    'lat': 0.699937,
    'lon': 122.446724,
    'cnt': 4,
    'units': 'metric' # to display temperature as Celsius
}
response = requests.get(url='http://api.openweathermap.org/data/2.5/forecast', params=parameter)
response.raise_for_status()
# print(response.status_code)

data = response.json()
list = data['list']
bring_umbrella = ""
for element in list:
    print(f"Time: {element['dt_txt']}")
    print(f"Description: {element['weather'][0]['description']}")
    print(f"Temperature: {element['main']['temp']}°C")
    print("--------------------")
    if element['weather'][0]['id'] < 800:
        bring_umbrella = "BRING AN UMBRELLA!"
print(bring_umbrella)
