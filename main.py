from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import json

from game import Game
from client_manager import ClientManager

app = FastAPI()
game = Game()
clients = ClientManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome! Guess the nuber between 1 to 100.")

    client = await clients.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            try:
                guess_data = json.loads(data)
                guess = guess_data.get("guess")

                if not isinstance(guess, int):
                    await websocket.send_text("Invalid format: expected {'guess': number}")
                    continue

                result = game.check_guess(guess)
                await websocket.send_text(result)

                if result == "You guessed correct!":
                    client.wins += 1
                    await clients.broadcast(
                        f"{client.name} guessed the number {guess}!", exclude=client.id
                    )
                    await asyncio.sleep(5)
                    game.reset()
                    await clients.broadcast("A new game has begun!")
                    await websocket.send_text("A new game has begun!")
            except json.JSONDecodeError:
                await websocket.send_text("Error JSON.")
    except WebSocketDisconnect:
        clients.disconnect(client.id)
        await clients.broadcast(f"{client.name} has disconnected.")
