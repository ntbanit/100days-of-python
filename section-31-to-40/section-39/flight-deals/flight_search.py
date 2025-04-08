import requests
import os 
from flight_data import FlightData

API_DOMAIN = 'https://test.api.amadeus.com'
API_ENDPOINT = '/v1/reference-data/locations/cities'
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.access_token = self.get_new_token()
    
    def get_iata_code(self, city_name):
        # Make a request to the Flight Search API with the provided parameters.
        # Return the response from the API.
        params = {
            'keyword': city_name,
            'max': 1
        }
        HEADERS = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(url=f'{API_DOMAIN}{API_ENDPOINT}', headers=HEADERS, params=params, verify=False)
        response.raise_for_status()

        return response.json()['data'][0]['iataCode']
    
    def find_cheapest_flight(self, origin, destination, departure_date, return_date):
        # This method will find the cheapest flight using the Flight Search API.
        # Return the response from the API.
        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': departure_date,
            'returnDate': return_date,
            'adults': 1,
            'currencyCode': 'EUR',
            'nonStop': 'true',
            'max': 250
        }
        HEADERS = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(url=f'{API_DOMAIN}/v2/shopping/flight-offers', headers=HEADERS, params=params, verify=False)
        response.raise_for_status()
        
        flights_data = response.json()['data']
        link = response.json()['meta']['links']['self']

        if not flights_data:
            return None

        cheapest_price = float(flights_data[0]['price']['total'])
        for flight in flights_data:
            cheapest_price = min (cheapest_price, float(flight['price']['total']))
        
        flights_data = FlightData(
            origin_city = origin,
            destination_city = destination,
            out_date = departure_date,
            return_date = return_date,
            price = cheapest_price,
            link = link
        )
        return flights_data

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
