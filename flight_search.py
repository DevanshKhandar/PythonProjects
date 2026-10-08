import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        response = requests.get(
            url="https://serpapi.com/search",
            params=parameters
        )

        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data}")

        return data