import requests
import os
SHEETY_DOMAIN = 'https://api.sheety.co/'
SHEETY_RANDOM_STRING = os.environ.get('SHEETY_RANDOM_STRING')
SHEETY_ENDPOINT = '/flightDealsAnTheCoder/prices'
API_ENDPOINT = f'{SHEETY_DOMAIN}/{SHEETY_RANDOM_STRING}{SHEETY_ENDPOINT}'
SHEETY_API_TOKEN = os.environ.get('SHEETY_API_TOKEN')
print(SHEETY_API_TOKEN)
HEADERS = {
    'Authorization': f'Bearer {SHEETY_API_TOKEN}',
}
class DataManager:
    def __init__(self):
        requests.packages.urllib3.disable_warnings()

    def fetch_data(self):
        response = requests.get(url=API_ENDPOINT, headers=HEADERS, verify=False)
        response.raise_for_status()
        data = response.json()
        
        return data['prices']

    def update_iata_code(self, data):
        for item in data:
            payload_data = {
                'price': {
                    'iataCode': item['iataCode'],
                    'lowestPrice': item['lowestPrice']
                }
            }
            response = requests.put(url=f'{API_ENDPOINT}/{item['id']}', headers=HEADERS, json=payload_data, verify=False)
            response.raise_for_status()
            

