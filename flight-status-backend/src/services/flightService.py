# import requests
# from config import Config
# from models.flightModel import Flight

# class FlightService:
#     @staticmethod
#     def get_flights(flight_number=None, airline_name=None, departure_iata=None, arrival_iata=None):
#         params = {
#             'access_key': Config.API_KEY,
#             'flight_iata': flight_number,
#             'airline_name': airline_name,
#             'dep_iata': departure_iata,
#             'arr_iata': arrival_iata
#         }

#         # Remove params with None values
#         params = {k: v for k, v in params.items() if v is not None}

#         response = requests.get(Config.API_URL, params=params)
#         print(f"API URL: {Config.API_URL}")
#         print(f"Params: {params}")
#         print(f"Response Status Code: {response.status_code}")
#         print(f"Response Content: {response.content}")

#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 print(f"Response JSON: {data}")

#                 if data and 'data' in data:
#                     flights_data = data['data']
#                     print(f"Number of flights found: {len(flights_data)}")
#                     flights = []
#                     for flight in flights_data:
#                         try:
#                             flight_obj = Flight.from_dict(flight)
#                             print(f"Processed flight: {flight_obj.__dict__}")
#                             flights.append(flight_obj)
#                         except Exception as e:
#                             print(f"Error processing flight data: {flight}, Error: {e}")
#                     return flights
#                 else:
#                     raise ValueError("Unexpected response structure or 'data' key missing.")
#             except Exception as e:
#                 print(f"Error parsing response JSON: {e}")
#                 raise
#         else:
#             print(f"API Request failed with status code: {response.status_code}")
#             response.raise_for_status()


import requests
from config import Config
from models.flightModel import Flight

class FlightService:
    @staticmethod
    def get_flights(flight_number=None, airline_name=None, departure_iata=None, arrival_iata=None):
        params = {
            'access_key': Config.API_KEY,
            'flight_iata': flight_number,
            'airline_name': airline_name,
            'dep_iata': departure_iata,
            'arr_iata': arrival_iata
        }

        # Debugging: Print out the parameters before filtering
        print(f"Original parameters: {params}")

        # Remove parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        # Debugging: Print out the parameters after filtering
        print(f"Filtered parameters: {params}")

        try:
            print(f"Requesting flights with parameters: {params}")
            response = requests.get(Config.API_URL, params=params)
            response.raise_for_status()  # Raise an error for 4xx/5xx responses

            data = response.json()
            if 'data' in data:
                flights_data = data['data']
                flights = [Flight.from_dict(flight) for flight in flights_data]
                return flights
            else:
                raise ValueError("Unexpected response structure or 'data' key missing.")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching flight data: {e}")
            raise

        except ValueError as ve:
            print(f"Data processing error: {ve}")
            raise
