from add_header import add_header

def convert_response(response):
    if isinstance(response, str):
        response = response.encode('iso-8859-1')

    sep = b"\r\n\r\n"
    index = response.find(sep)
    if index == -1:
        return response

    header_block = response[:index]
    body = response[index + len(sep):]

    header_text = header_block.decode('iso-8859-1')
    lines = header_text.split('\r\n')
    status_line = lines[0]
    headers = lines[1:]

    headers = add_header(headers, 'X-Proxy-Server', 'Custom Proxy')

    content_length = len(body)
    new_headers = []
    found_cl = False
    for header in headers:
        if header.lower().startswith('content-length'):
            new_headers.append(f"Content-Length: {content_length}")
            found_cl = True
        else:
            new_headers.append(header)
    if not found_cl:
        new_headers.append(f"Content-Length: {content_length}")

    header_bytes = (status_line + '\r\n' + '\r\n'.join(new_headers) + '\r\n\r\n').encode('iso-8859-1')

    return header_bytes + body