from flask import Blueprint, request, jsonify
from controllers.flightController import FlightController

flight_routes = Blueprint('flight_routes', __name__)

@flight_routes.route('/api/search_flights', methods=['GET'])
def search_flights():
    flight_number = request.args.get('flight_number')
    airline_name = request.args.get('airline_name')
    departure_iata = request.args.get('dep_iata')  # Matching the param name
    arrival_iata = request.args.get('arr_iata')  # Matching the param name

    print(f"Departure IATA: {departure_iata}")
    print(f"Arrival IATA: {arrival_iata}")

    try:
        flights = FlightController.get_flights(flight_number, airline_name, departure_iata, arrival_iata)
        flight_list = [flight.__dict__ for flight in flights]
        return jsonify(flight_list)
    except Exception as e:
        print(f"Error in search_flights route: {e}")
        return jsonify({'error': str(e)}), 500