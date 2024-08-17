#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

FLIGHT_ORIGIN = 'LON'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])

    data_manager.update_sheet_data(sheet_data)
    data_manager.update_iata_codes()
    sheet_data = data_manager.get_sheet_data()

for row in sheet_data:
    print(f"Getting flights for {row['city']}...")
    flights = flight_search.get_flights(FLIGHT_ORIGIN, row["iataCode"])
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{row['city']}: £{cheapest_flight.price}")

    if cheapest_flight.price != 0 and cheapest_flight.price < row["lowestPrice"]:
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )