import uuid


class Client:
    def __init__(self, websocket, name=None):
        self.id = str(uuid.uuid4())[:8]
        self.websocket = websocket
        self.name = name or f"Player #{self.id}"
        self.wins = 0


class ClientManager:
    def __init__(self):
        self.clients = {}

    async def connect(self, websocket, name=None):
        client = Client(websocket, name)
        self.clients[client.id] = client
        return client

    def disconnect(self, client_id):
        self.clients.pop(client_id, None)

    async def broadcast(self, message: str, exclude: str = None):
        for cid, client in self.clients.items():
            if cid != exclude:
                await client.websocket.send_text(message)

    def get_all(self):
        return list(self.clients.values())
