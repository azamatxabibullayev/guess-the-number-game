import asyncio
import json
import websockets


async def guess_number():
    uri = "ws://localhost:8000/ws"

    try:
        async with websockets.connect(uri) as ws:
            greeting = await ws.recv()
            print("Server:", greeting)
            while True:
                raw = input("Your number: ")
                try:
                    guess = int(raw)
                except ValueError:
                    print("Please enter an integer.")
                    continue

                await ws.send(json.dumps({"guess": guess}))
                reply = await ws.recv()
                print("Server:", reply)
                if "угадали" in reply.lower() or "correct" in reply.lower():
                    continue

    except websockets.ConnectionClosed:
        print("Connection closed by server.")


if __name__ == "__main__":
    asyncio.run(guess_number())
