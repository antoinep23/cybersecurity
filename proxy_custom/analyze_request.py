from decode_data import decode_data
from rate_limite import rate_limit

def analyze_request(request):
    decoded_request = decode_data(request)

    if rate_limit(decoded_request) != "OK":
        return "429"
    
    elif decoded_request['request_line'].lower() == '/admin':
        return "403"

    return "OK"