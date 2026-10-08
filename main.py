import requests_cache

requests_cache.install_cache(
    "flight_cache",
    backend="sqlite",
    expire_after=3600
)

from datetime import datetime, timedelta
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


# ==================== Set the Dates ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

tomorrow = tomorrow.strftime("%Y-%m-%d")
six_month_from_today = six_month_from_today.strftime("%Y-%m-%d")


# ==================== Get Sheet Data ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


# ==================== Flight Search ====================

flight_search = FlightSearch()

for destination in sheet_data:

    flights = flight_search.check_flights(
        origin_city_code="LHR",
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(
        flights,
        return_date=six_month_from_today
    )

    if cheapest_flight.price != "N/A":

        print(
            f"{destination['city']}: GBP {cheapest_flight.price}"
        )

        if cheapest_flight.price < destination["lowestPrice"]:

            print(
                f"Lower price flight found to {destination['city']}!"
            )

            data_manager.update_lowest_price(
                row_id=destination["id"],
                new_price=cheapest_flight.price
            )