import requests
import os 
API_DOMAIN = 'https://test.api.amadeus.com'
API_ENDPOINT = '/v1/security/oauth2/token'
# API_ENDPOINT = '/v1/flights/v1/search'
HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
data = {
    'grant_type': 'client_credentials',
    'client_id': f'{client_id}',
    'client_secret': f'{client_secret}'
}
requests.packages.urllib3.disable_warnings()
response = requests.post(url=f'{API_DOMAIN}{API_ENDPOINT}', headers=HEADERS, data=data, verify=False)
response.raise_for_status()
data = response.json()
print(data)
access_token = data['access_token']

print(access_token)

API_ENDPOINT = '/v1/reference-data/locations/cities'
params = {
    # 'countryCode': 'FR',
    'keyword': 'Hanoi',
    'max': 1
}
HEADERS = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get(url=f'{API_DOMAIN}{API_ENDPOINT}', headers=HEADERS, params=params, verify=False)
response.raise_for_status()

data = response.json()
# print(data)
import json
print(json.dumps(data, indent=4))