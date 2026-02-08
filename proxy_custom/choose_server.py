import asyncio
import uuid

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
    tasks = [test_server(server) for server in servers.values()]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    healthy_servers = [server for server, result in zip(servers.values(), results) if result is True]
   
    if healthy_servers:
        chosen_server = min(healthy_servers, key=lambda s: s['last_hit'])
        chosen_server['last_hit'] += 1
        return chosen_server
    
    return None