import os

import requests
import json
from datetime import datetime
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

ENDPOINT = os.environ.get('ENDPOINT')

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

basic = HTTPBasicAuth(USERNAME, PASSWORD)

workout = input("Enter your workout: ")

params = {
    "query": workout
}

response = requests.post(url=ENDPOINT, json=params, headers=headers)

exercises = json.loads(response.text)

today = datetime.now()

date = str(today.strftime('%d/%m/%Y'))
time_now = str(today.strftime('%H:%M:%S'))

for exercise in exercises['exercises']:
    workout = {
        "workout": {
            "date": date,
            "time": time_now,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    response = requests.post(url='https://api.sheety.co/536044117d5d5c13aa5d3149fe216038/workouts/workouts',
                             json=workout, auth=basic)
    print(response.text)

