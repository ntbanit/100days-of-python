#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
sheet_data = dm.fetch_data()
print(sheet_data)

fs = FlightSearch()
for sheet in sheet_data :
    if not sheet['iataCode']:
        iata_code = fs.get_iata_code(sheet['city'])
        sheet['iataCode'] = iata_code

print(sheet_data)
dm.update_iata_code(sheet_data)