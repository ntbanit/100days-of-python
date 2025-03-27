import requests
import json
from datetime import datetime
import os

API_DOMAIN = 'https://trackapi.nutritionix.com'
API_ENDPOINT = '/v2/natural/exercise'

MY_APP_ID = os.environ.get('MY_APP_ID')
MY_API_KEY = os.environ.get('MY_API_KEY')

HEADERS = {
    'x-app-id': MY_APP_ID,
    'x-app-key': MY_API_KEY,
    'Content-Type': 'application/json'
}

payload_data = {
    'query': input('What is your workout? Eg. Yoga in 30 minutes and running 2km\n'),
    'gender': 'female',
    'weight_kg': 51,
    'height_cm': 153,
    'age': 31
}
requests.packages.urllib3.disable_warnings()
response = requests.post(url=f'{API_DOMAIN}{API_ENDPOINT}', headers=HEADERS, json=payload_data, verify=False)
response.raise_for_status()
print(json.dumps(response.json(), indent=4))

exercise_data = response.json()['exercises'][0]

exercise_name = exercise_data['name']
duration_min = exercise_data['duration_min']
nf_calories = exercise_data['nf_calories']

today = datetime.now()
today_date = today.strftime('%Y-%m-%d')
today_time = today.strftime('%X')
print(today_date)
print(today_time)

SHEETY_API_URL = 'https://api.sheety.co'
SHEETY_RANDOM_STR = os.environ.get('SHEETY_RANDOM_STR')
SHEETY_ENDPOINT = f'/{SHEETY_RANDOM_STR}/anNguyenDailyYoga/workouts'
MY_SUPER_SECRET_TOKEN = os.environ.get('MY_SUPER_SECRET_TOKEN')
headers = {
    'Authorization': f'Bearer {MY_SUPER_SECRET_TOKEN}',
    'Content-Type': 'application/json'
}

payload_data = {
    'workout': {
        'date': today_date,
        'time': today_time,
        'exercise': exercise_name,
        'duration': duration_min,
        'calories': nf_calories
    }
}
response = requests.post(url=f'{SHEETY_API_URL}{SHEETY_ENDPOINT}', json=payload_data, headers=headers, verify=False)
response.raise_for_status()
print(json.dumps(response.json(), indent=4))