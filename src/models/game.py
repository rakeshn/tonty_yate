import uuid


class Game:
    def __init__(self):
        self.players = []
        self.id = str(uuid.uuid4().hex)
        self.deck = []


