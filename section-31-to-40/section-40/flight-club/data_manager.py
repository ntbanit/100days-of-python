import os
import requests

class DataManager:

    def __init__(self):
        self.header = f"Bearer {os.environ.get('SHEETY_API_TOKEN')}"
        self.SHEETY_PRICES_ENDPOINT = os.environ.get('SHEETY_PRICES_ENDPOINT')
        self.SHEETY_USERS_ENDPOINT = os.environ.get('SHEETY_USERS_ENDPOINT')
        print(f"header:\n {self.header}")
        print(f"SHEETY_PRICES_ENDPOINT:\n {self.SHEETY_PRICES_ENDPOINT}")
        print(f"SHEETY_USERS_ENDPOINT:\n {self.SHEETY_USERS_ENDPOINT}")
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT, headers={"Authorization": self.header}, verify=False)
        data = response.json()
        self.destination_data = data["prices"]
        
        return self.destination_data
    
    def get_user_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=self.SHEETY_USERS_ENDPOINT, headers={"Authorization": self.header}, verify=False)
        data = response.json()
        self.user_data = data["users"]
        
        return self.user_data


    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.packages.urllib3.disable_warnings()
            response = requests.put(
                url=f"{self.SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers={"Authorization": self.header},
                json=new_data, 
                verify=False
            )
            print(response.text)

#TESTING
data_manager = DataManager()
sheet_data = data_manager.get_user_data()
for data in sheet_data:
    print(data['email'])
print(sheet_data)