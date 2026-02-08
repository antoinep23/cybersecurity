import asyncio
from redirect import redirect_request
from convert_response import convert_response
from analyze_request import analyze_request


PORT = 8888

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr} has been established")

    while True:
        data = await reader.read(4096)
        if not data:
            break

        check_status = analyze_request(data)
        if check_status != "OK":
            
            if check_status == "403":
                writer.write(bytes("HTTP/1.1 403 Forbidden\r\n\r\n403: Forbidden", 'utf-8'))

            elif check_status == "429":
                writer.write(bytes("HTTP/1.1 429 Too Many Requests\r\n\r\n429: Too Many Requests", 'utf-8'))

            else:
                writer.write(bytes("HTTP/1.1 400 Bad Request\r\n\r\n400: Bad Request", 'utf-8'))

            await writer.drain()
            break
        
        received_data = await redirect_request(data)

        if received_data:
            converted_response = convert_response(received_data)
            writer.write(bytes(converted_response, 'utf-8'))
            await writer.drain()

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', PORT)
    
    print(f'HTTP Proxy Server is running on port {PORT} ✅')

    async with server:
        await server.serve_forever()


asyncio.run(main())