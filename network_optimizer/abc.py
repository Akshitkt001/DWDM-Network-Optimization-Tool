import asyncio
import websockets

async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/network-status/"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, world!")
        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.run(test_websocket())
