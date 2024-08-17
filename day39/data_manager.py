import os
import requests
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:

    def __init__(self):
        self.header = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
        }
        self.data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.header)
        data = response.json()
        self.data = data["prices"]
        return self.data

    def update_sheet_data(self, new_sheet_data):
        self.data = new_sheet_data

    def update_iata_codes(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=self.header)