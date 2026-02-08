from add_header import add_header
from decode_data import decode_data

def reconstruct_http(obj):
    status_line = f"HTTP/1.1 {obj['request_line']} OK\r\n"
    headers = "\r\n".join(obj['headers'])
    body = "".join(obj['body'])
    
    return f"{status_line}{headers}\r\n\r\n{body}"

def convert_response(response):
    object_response = decode_data(response)

    object_response['headers'] = add_header(object_response['headers'], 'X-Proxy-Server', 'Custom Proxy')

    content_length = sum(len(line) for line in object_response['body'])

    object_response['headers'] = [header if not header.startswith('Content-Length') else f"Content-Length: {content_length}" for header in object_response['headers']]

    return reconstruct_http(object_response)