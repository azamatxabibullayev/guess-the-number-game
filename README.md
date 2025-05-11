# Guess the Number - WebSocket Multiplayer Game

A multiplayer number guessing game built with **FastAPI** and **WebSockets**, where players connect via WebSocket and
try to guess a number between 1 and 100.

---

## Features

- Real-time WebSocket communication
- Randomly generated number per round
- Real-Time Feedback for each guess: higher/lower/correct
- Broadcasts to all connected players
- Easily extendable for user sessions, scores, etc.

---

## Requirements

- `Python 3.9+`
- `FastAPI`
- `uvicorn`
- `websockets`

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourname/guess_number_game.git
   cd guess_number_game

2. **Create and activate a virtual environment**

python3 -m venv .venv
source .venv/bin/activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Running the Server**
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

---

## Playing the Game (Client)

**Use the provided client**
python example_client.py

**You will see**

Server: Welcome! Guess the nuber between 1 to 100.
Your number:

**Then enter guesses (e.g. 50, 75) until you get it right!**