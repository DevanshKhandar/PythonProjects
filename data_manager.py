import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.username = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]

    def get_destination_data(self):
        response = requests.get(
            url=self.endpoint,
            auth=(self.username, self.password)
        )

        data = response.json()

        return data["prices"]

    def update_lowest_price(self, row_id, new_price):

        parameters = {
            "price": {
                "lowestPrice": new_price
            }
        }

        response = requests.put(
            url=f"{self.endpoint}/{row_id}",
            json=parameters,
            auth=(self.username, self.password)
        )

        print(response.text)