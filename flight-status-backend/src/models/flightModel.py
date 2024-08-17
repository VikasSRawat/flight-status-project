class Flight:
    def __init__(self, airline_name, flight_iata, departure_airport, departure_iata, arrival_airport, arrival_iata, is_ground, departure_actual, departure_estimated, arrival_scheduled, arrival_actual):
        self.airline_name = airline_name
        self.flight_iata = flight_iata
        self.departure_airport = departure_airport
        self.departure_iata = departure_iata
        self.arrival_airport = arrival_airport
        self.arrival_iata = arrival_iata
        self.is_ground = is_ground
        self.departure_actual = departure_actual
        self.departure_estimated = departure_estimated
        self.arrival_scheduled = arrival_scheduled
        self.arrival_actual = arrival_actual

    @staticmethod
    def from_dict(data):
        airline = data.get('airline', {})
        flight = data.get('flight', {})
        departure = data.get('departure', {})
        arrival = data.get('arrival', {})
        live = data.get('live', {})

        return Flight(
            airline_name=airline.get('name', 'Unknown Airline'),
            flight_iata=flight.get('iata', 'Unknown IATA'),
            departure_airport=departure.get('airport', 'Unknown Airport'),
            departure_iata=departure.get('iata', 'Unknown IATA'),
            arrival_airport=arrival.get('airport', 'Unknown Airport'),
            arrival_iata=arrival.get('iata', 'Unknown IATA'),
            is_ground=live.get('is_ground', True) if live else True,
            departure_actual=departure.get('actual', 'Unknown'),
            departure_estimated=departure.get('estimated', 'Unknown'),
            arrival_scheduled=arrival.get('scheduled', 'Unknown'),
            arrival_actual=arrival.get('actual', 'Unknown')
        )
