import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
AMADEUS_ENDPOINT = os.getenv("AMADEUS_ENDPOINT")
AMADEUS_ENDPOINT_V2 = os.getenv("AMADEUS_ENDPOINT_V2")
AMADEUS_TOKEN_ENDPOINT = f"{AMADEUS_ENDPOINT}/security/oauth2/token"
AMADEUS_CITY_ENDPOINT = f"{AMADEUS_ENDPOINT}/reference-data/locations/cities"
AMADEUS_FLIGHT_ENDPOINT = f"{AMADEUS_ENDPOINT_V2}/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self.api_key = os.environ["AMADEUS_API_KEY"]
        self.api_secret = os.environ["AMADEUS_API_SECRET"]
        self.token = self.get_new_token()

    def get_iata_code(self, city_name):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        parameters = {
            "keyword": city_name,
            "include": "AIRPORTS",
        }
        response = requests.get(url=AMADEUS_CITY_ENDPOINT, headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]

    def get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=headers, data=data)
        response.raise_for_status()
        return response.json()['access_token']

    def get_flights(self, origin, destination):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        parameters = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': datetime.now().strftime('%Y-%m-%d'),
            "returnDate": (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'adults': 1,
            "nonStop": "true",
            'currencyCode': 'USD',
        }
        response = requests.get(url=AMADEUS_FLIGHT_ENDPOINT, headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()