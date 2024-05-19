from flask import Flask, request, jsonify
import geoip2.database

app = Flask(__name__)

# Path to the GeoIP2 database
GEOIP_DB_PATH = "GeoLite2-Country.mmdb"

# Function to get country code from IP address using GeoIP
def get_country_code(ip):
    with geoip2.database.Reader(GEOIP_DB_PATH) as reader:
        try:
            response = reader.country(ip)
            country_code = response.country.iso_code
            return country_code
        except geoip2.errors.AddressNotFoundError:
            return None

# Route to handle GET requests with IP address parameter
@app.route('/', methods=['GET'])
def get_country():
    ip_address = request.args.get('ip')
    if ip_address is None:
        return jsonify({"error": "IP address parameter missing"}), 400

    country_code = get_country_code(ip_address)
    if country_code:
        return jsonify({"ip": ip_address, "country": country_code}), 200
    else:
        return jsonify({"error": "Could not find country for the given IP address"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

