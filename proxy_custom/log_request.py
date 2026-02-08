import datetime


def log_request(request):
    current_day = datetime.datetime.now().strftime("%Y-%m-%d")

    log_entry = f"{datetime.datetime.now()} - {request['request_line']} - {request['headers'][0].split()[1]}"

    with open(f"logs/log_{current_day}.log", "a") as log_file:
        log_file.write(log_entry + "\n")
    
    return