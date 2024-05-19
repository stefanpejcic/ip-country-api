from flask import Flask, request, jsonify
import geoip2.database
import os

app = Flask(__name__)

# Path to the GeoIP2 database
GEOIP_DB_PATH = "GeoLite2-Country.mmdb"

# Function to check if GeoIP2 database exists
def check_database_exists():
    return os.path.exists(GEOIP_DB_PATH)

# Function to get country code from IP address using GeoIP
def get_country_code(ip):
    with geoip2.database.Reader(GEOIP_DB_PATH) as reader:
        try:
            response = reader.country(ip)
            country_code = response.country.iso_code
            return country_code
        except geoip2.errors.AddressNotFoundError:
            return None

# Route to handle GET requests with optional IP address in the path
@app.route('/', defaults={'ip': None})
@app.route('/<ip>', methods=['GET'])
def get_country(ip):
    # If no IP is provided in the path, use the requester's IP address
    if ip is None:
        ip = request.remote_addr

    country_code = get_country_code(ip)
    if country_code:
        response = jsonify({"ip": ip, "country": country_code})
        # Set cache-control headers to enable client-side caching for 24 hours (86400 seconds)
        response.headers['Cache-Control'] = 'public, max-age=86400'
        return response, 200
    else:
        return jsonify({"error": "Could not find country for the given IP address"}), 404

# Health check endpoint
@app.route('/health')
def health_check():
    if check_database_exists():
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error", "message": "GeoIP2 database not found"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
