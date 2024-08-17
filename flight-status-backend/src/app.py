from flask import Flask
from flask_cors import CORS
from routes.flightRoutes import flight_routes

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register blueprint
app.register_blueprint(flight_routes)

if __name__ == '__main__':
    app.run(debug=True)

