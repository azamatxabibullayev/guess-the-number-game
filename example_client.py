import asyncio
import websockets
import json


async def guess_number():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        async def send():
            while True:
                guess = input("Your number: ")
                try:
                    await websocket.send(json.dumps({"guess": int(guess)}))
                except ValueError:
                    print("Please enter an integer.")

        async def receive():
            while True:
                message = await websocket.recv()
                print("Server:", message)

        await asyncio.gather(send(), receive())


asyncio.run(guess_number())
