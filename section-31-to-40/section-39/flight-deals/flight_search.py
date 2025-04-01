import requests
import os 
API_DOMAIN = 'https://test.api.amadeus.com'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.access_token = self.get_new_token()
    
    def get_iata_code(self, city):
        # Make a request to the Flight Search API with the provided parameters.
        # Return the response from the API.
        return "TESTING_CODE"

    def get_new_token(self):
        HEADERS = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': f'{client_id}',
            'client_secret': f'{client_secret}'
        }
        response = requests.post(url=f'{API_DOMAIN}/v1/security/oauth2/token', headers=HEADERS, data=data, verify=False)
        response.raise_for_status()
        return response.json()['access_token']
