import asyncio
import uuid
import os

servers = {
    'server1': {
        'ip': '127.0.0.1',
        'port': 7777,
        'id': str(uuid.uuid4()),
        'last_hit': 0
    },
    'server2': {
        'ip': '127.0.0.1',
        'port': 7778,
        'id': str(uuid.uuid4()),
        'last_hit': 0
    },
    'server3': {
        'ip': '127.0.0.1',
        'port': 7779,
        'id': str(uuid.uuid4()),
        'last_hit': 0
    }
}

async def get_healthy_servers_list():
    tasks = [test_server(server) for server in servers.values()]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    healthy_servers = [server for server, result in zip(servers.values(), results) if result is True]

    return healthy_servers

def get_run_server_command(port): 
    return f"python3 -m http.server {port}"

async def test_server(server):
    try:
        _, writer = await asyncio.wait_for(
            asyncio.open_connection(server['ip'], server['port']), 
            timeout=1.0
        )
        writer.close()
        await writer.wait_closed()
        return True
    except:
        return False

async def choose_server():
    healthy_servers = await get_healthy_servers_list()

    if not healthy_servers:
        for server in servers.values():
            command = get_run_server_command(server['port'])
            asyncio.create_task(asyncio.to_thread(lambda: os.system(command)))
            await asyncio.sleep(2)

        healthy_servers = await get_healthy_servers_list()

   
    if healthy_servers:
        chosen_server = min(healthy_servers, key=lambda s: s['last_hit'])
        chosen_server['last_hit'] += 1
        return chosen_server
    
    return None