import asyncio
async def tcp_client():
    host = '127.0.0.1' 
    port = 7788 
    reader, writer = await asyncio.open_connection(host, port)
    print(f"Connected to server at {host}:{port}")   
    while True:
        message = input("Enter your message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Closing connection...")
            break           
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(1024)
        print(f"Received from server: {data.decode()}")
    writer.close()
    await writer.wait_closed()
    print("Connection closed.")
asyncio.run(tcp_client())