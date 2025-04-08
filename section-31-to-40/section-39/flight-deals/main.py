#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
dm = DataManager()
sheet_data = dm.fetch_data()
# print(sheet_data)

fs = FlightSearch()
need_update = False
for sheet in sheet_data :
    if not sheet['iataCode']:
        need_update = True
        iata_code = fs.get_iata_code(sheet['city'])
        sheet['iataCode'] = iata_code

# print(sheet_data)
if need_update:
    print("Updating IATA codes...")
    dm.update_iata_code(sheet_data)

notif = NotificationManager()
tomorrow = datetime.now() + timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')
six_months_later = datetime.now() + timedelta(days=180)
six_months_later = six_months_later.strftime('%Y-%m-%d')
LONDON_IATA_CODE = 'LON'
need_update = False
for sheet in sheet_data :
    current_price = float(sheet['lowestPrice'])
    flight = fs.find_cheapest_flight(LONDON_IATA_CODE, sheet['iataCode'], tomorrow, six_months_later)
    if flight and flight.price < current_price:
        print(f"Found a cheaper flight to {sheet['city']} for {flight.price} EUR!")
        notif.send_email(flight_data=flight)
        sheet['lowestPrice'] = flight.price
        need_update = True
    else:
        print(f"Found a flight to {sheet['city']} for {flight.price if flight else current_price} EUR.")
        print(f"Current price is {current_price} EUR, no need to update.")
        print(f"No cheaper flight found to {sheet['city']}")

if need_update:
    print("Updating Prices...")
    dm.update_iata_code(sheet_data)