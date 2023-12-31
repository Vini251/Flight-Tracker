from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5cdbe1f462e77f7fee6410bdddee27df/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/5cdbe1f462e77f7fee6410bdddee27df/flightDeals/user"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USER_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["user"]
        return self.customer_data