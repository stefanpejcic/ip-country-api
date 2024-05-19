import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'GET' and environ['PATH_INFO'] == '/health':
        return health_check(environ, start_response)
    elif environ['REQUEST_METHOD'] == 'GET':
        ip_address = environ.get('PATH_INFO').lstrip('/')
        return get_country(environ, start_response, ip_address)
    else:
        start_response('405 Method Not Allowed', [('Content-Type', 'text/plain')])
        return [b'Method Not Allowed']


def check_database_exists():
    return os.path.exists("GeoLite2-Country.mmdb")


def get_country_code(ip):
    import geoip2.database

    with geoip2.database.Reader("GeoLite2-Country.mmdb") as reader:
        try:
            response = reader.country(ip)
            country_code = response.country.iso_code
            return country_code
        except geoip2.errors.AddressNotFoundError:
            return None


def health_check(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    response = ''
    if check_database_exists():
        response = '{"status": "ok"}'
    else:
        status = '500 Internal Server Error'
        response = '{"status": "error", "message": "GeoIP2 database not found"}'
    start_response(status, headers)
    return [response.encode()]


def get_country(environ, start_response, ip):
    if ip == '':
        ip = environ['REMOTE_ADDR']

    country_code = get_country_code(ip)
    if country_code:
        status = '200 OK'
        headers = [('Content-type', 'application/json')]
        response = '{"ip": "%s", "country": "%s"}' % (ip, country_code)
    else:
        status = '404 Not Found'
        response = '{"error": "Could not find country for the given IP address"}'

    start_response(status, headers)
    return [response.encode()]
