class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data, return_date):
    try:
        # Combine best_flights and other_flights
        all_flights = data.get("best_flights", []) + data.get("other_flights", [])

        if not all_flights:
            return FlightData(
                price="N/A",
                origin_airport="N/A",
                destination_airport="N/A",
                out_date="N/A",
                return_date="N/A"
            )

        cheapest_flight = None
        cheapest_price = float("inf")

        for flight in all_flights:
            try:
                price = flight["price"]

                if price < cheapest_price:
                    cheapest_price = price

                    origin_airport = flight["flights"][0]["departure_airport"]["id"]
                    destination_airport = flight["flights"][-1]["arrival_airport"]["id"]

                    out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

                    cheapest_flight = FlightData(
                        price=price,
                        origin_airport=origin_airport,
                        destination_airport=destination_airport,
                        out_date=out_date,
                        return_date=return_date
                    )

            except (KeyError, TypeError):
                # Skip flights where price or required information is missing
                continue

        if cheapest_flight is None:
            return FlightData(
                price="N/A",
                origin_airport="N/A",
                destination_airport="N/A",
                out_date="N/A",
                return_date="N/A"
            )

        return cheapest_flight

    except (KeyError, TypeError):
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A"
        )