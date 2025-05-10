import random
import asyncio


class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.active = True

    def check_guess(self, guess: int) -> str:
        if not self.active:
            return "Wait for new game..."
        if guess < self.secret_number:
            return "More"
        elif guess > self.secret_number:
            return "Less"
        else:
            self.active = False
            return "You guessed right !"
