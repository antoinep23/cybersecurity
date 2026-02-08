import asyncio
from choose_server import choose_server

async def redirect_request(data):
    server = await choose_server()
    if server is None:
        return "HTTP/1.1 503 Service Unavailable\r\n\r\nNo healthy backends available"

    try:
        reader, writer = await asyncio.open_connection(server['ip'], server['port'])
        
        writer.write(data)
        await writer.drain()
        
        received = await reader.read(4096)
        
        writer.close()
        await writer.wait_closed()
        
        return received.decode("utf-8")
    
    except Exception as e:
        print(f"Failed to redirect to {server['ip']}: {e}")
        return None