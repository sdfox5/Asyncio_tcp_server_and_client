import asyncio
async def client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected with: {addr}")
    while True:
        data = await reader.read(1024) 
        if not data:
            print(f"Connection with {addr} closed.\n")
            break
        print(f"Received: {data.decode()} from client {addr}")
        writer.write("Fox is back!".encode())
        await writer.drain()
    writer.close()
    await writer.wait_closed()
    print(f"Connection with {addr} is fully closed.")
async def main():
    host = '127.0.0.1'
    port = 7788
    server = await asyncio.start_server(client, host, port)
    print(f"Server is listening on {host}:{port}")
    async with server:
        await server.serve_forever()
asyncio.run(main())