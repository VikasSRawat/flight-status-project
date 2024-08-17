from flask import Blueprint, jsonify, request
from services.flightService import FlightService

# class FlightController:
#     @staticmethod
#     def get_flights(flight_number=None, airline_name=None, departure_iata=None, arrival_iata=None):
#         return FlightService.get_flights(flight_number, airline_name, departure_iata, arrival_iata)

class FlightController:
    @staticmethod
    def get_flights(flight_number=None, airline_name=None, departure_iata=None, arrival_iata=None):
        return FlightService.get_flights(flight_number, airline_name, departure_iata, arrival_iata)