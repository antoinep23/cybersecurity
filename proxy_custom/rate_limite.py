import datetime


request_list = {}
request_limit_per_minute = 20

def cleanup_request_list(host_address):
    if (len(request_list[host_address]) > request_limit_per_minute):
        request_list[host_address] = request_list[host_address][-request_limit_per_minute:]
    return

def rate_limit(request):
    current_time = datetime.datetime.now()
    host_address = request['headers'][0].split()[1]

    if host_address not in request_list:
        request_list[host_address] = []

    request_list[host_address].append(current_time)

    requests_inside_limit = request_list[host_address][-request_limit_per_minute:]

    if len(requests_inside_limit) >= request_limit_per_minute and requests_inside_limit[0] > (current_time - datetime.timedelta(minutes=1)):
        return "429"
    
    cleanup_request_list(host_address)
    return "OK"