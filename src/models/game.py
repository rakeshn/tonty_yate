import uuid

from src.models.deck import RANKS


class Game:
    def __init__(self):
        self.players = []
        self.id = str(uuid.uuid4().hex)
        self.deck = []
        self.trump = None
        self.trump_called = False

    def assign_trump(self, card):
        self.trump = card

    def call_trump(self):
        self.trump_called = True

class Round:
    def __init__(self, game):
        self.cards = []
        self.index_of_trump = 0
        self.players = []
        self.game = game

    def highest_card_index(self):
        highest_index = 99
        card_index = counter = 0 # if self.index_of_trump == 0 else self.index_of_trump
        valid_suit = self.cards[0].suit

        if self.game.trump_called is True and any(self.game.trump.suit in c.suit for c in self.cards[self.index_of_trump:]):
            valid_suit = self.game.trump.suit

        for card in self.cards:
            if card.suit is valid_suit and highest_index > RANKS.index(card.rank):
                highest_index = RANKS.index(card.rank)
                card_index = counter
            counter += 1
        return card_index

    def call_trump(self):
        self.index_of_trump = len(self.cards)
        self.game.call_trump()


    def play(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    def end(self):
        score = _score(self.cards)
        winner = self.players[self.highest_card_index()]
        return winner, score

_points = lambda rank: 3 if rank == 'Jack' else 2 if rank == '9' else 1 if rank in ['Ace', '10'] else 0
_score = lambda cards: sum(_points(card.rank) for card in cards)



