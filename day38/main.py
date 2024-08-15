import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

EXERCISE_API_ENDPOINT = os.environ.get("EXERCISE_API_ENDPOINT")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
parameters = {
    "query": text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
exercises = data["exercises"]

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
for exercise in exercises:
    headers = {
        "Authorization" : f"Bearer {SHEETY_TOKEN}"
    }
    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=parameters)
    response.raise_for_status()
    print(response.json())