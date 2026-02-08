def decode_data(data):
    decoded_response = data

    if isinstance(data, bytes):
        decoded_response = data.decode('utf-8')

    object_response = {
        'request_line': decoded_response.splitlines()[0].split()[1],
        'headers': decoded_response.splitlines()[1:decoded_response.splitlines().index('')],
        'body': decoded_response.splitlines()[decoded_response.splitlines().index('') + 1:]
    }
    

    return object_response