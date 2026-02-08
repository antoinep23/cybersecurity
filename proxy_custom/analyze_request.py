from decode_data import decode_data
from rate_limite import rate_limit
from log_request import log_request

def analyze_request(request, address):
    decoded_request = decode_data(request)

    log_request(decoded_request, address)

    if rate_limit(decoded_request) != "OK":
        return "429"
    
    elif decoded_request['request_line'].lower() == '/admin':
        return "403"

    return "OK"