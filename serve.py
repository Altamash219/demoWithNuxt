import asyncio
import websockets

connected = set()


async def test(websocket, path):
    print("server started")
    connected.add(websocket)

    # message=await websocket.recv()
    # print(message)
    try:
        async for message in websocket:
            print(message)
            print("Connect set", connected)
            for ws in connected:
                if ws != websocket:
                    await ws.send(message)
    finally:
        connected.remove(websocket)
start_server = websockets.serve(test, 'localhost', 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# while(True):
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()
