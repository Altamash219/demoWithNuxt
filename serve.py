import asyncio
import websockets

connected = set()


def emotioninput():
    return input("Enter emotion")


async def test(websocket, path):
    print("server started")
    connected.add(websocket)

    # message=await websocket.recv()
    # print(message)
    # em=input("Enter number spelling")
    try:
        async for message in websocket:
            print(message)
            for ws in connected:
                if ws != websocket:
                    await ws.send(message)
    finally:
        connected.remove(websocket)
    # while(True):
    #     emotion=input("Enter message")You should consider upgrading via the '/home/sankalp/anaconda3/bin/python3 -m pip install --upgrade pip' command.

    #     await websocket.send(emotion.strip(' '))
    # emotion=emotioninput()
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)
start_server = websockets.serve(test, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# while(True):
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()
