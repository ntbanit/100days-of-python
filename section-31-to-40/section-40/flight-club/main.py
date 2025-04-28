import re
def valid_email(email):
    """
    Validates an email address using a regular expression.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_user_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================
changed = False
for row in sheet_data:
    if row["iataCode"] == "":
        changed = True
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
if changed:
    data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
tested = False # ONLY SEND 1 EMAIL IS ENOUGH ! NO SPAMMING
for destination in sheet_data:
    if tested :
        break 
    print(f"Getting flights for {destination['city']}...")
    nonstop_flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(nonstop_flights)
    stop_flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        nonstop=False
    )
    another_cheapest_flight = find_cheapest_flight(stop_flights)
    if another_cheapest_flight.price < cheapest_flight.price:
        cheapest_flight = another_cheapest_flight

    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        tested = True
        print(f"Lower price flight found to {destination['city']}!")
        for client in customer_data:
            test_client_email = client["email"]
            if not valid_email(test_client_email) :
                continue

            print(f"Sending email to {test_client_email}...")
            # Send mail for simplify notification
            notification_manager.send_email(
                client_email = test_client_email,
                mail_title = "Low price alert!",
                message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                            f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )


