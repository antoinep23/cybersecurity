def add_header(headers, header_name, header_value):
    header_line = f"{header_name}: {header_value}"
    headers.append(header_line)
    return headers