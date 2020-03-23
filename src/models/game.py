import uuid

from src.models.deck import RANKS


class Game:
    def __init__(self):
        self.players = []
        self.id = str(uuid.uuid4().hex)
        self.deck = []


class Round:
    def __init__(self):
        self.cards = []
        self.index_of_trump = 0
        self.players = []

    def call_trump(self):
        self.index_of_trump = len(self.cards)

    def play(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    def end(self):
        score = _score(self.cards)
        winner = self.players[highest_card_index(self.cards, self.index_of_trump)]
        return winner, score


_points = lambda rank: 3 if rank == 'Jack' else 2 if rank == '9' else 1 if rank == 'Ace' else 1 if rank == '10' else 0
_score = lambda cards: sum(_points(card.rank) for card in cards)


def highest_card_index(cards, trump_idx):
    highest_index = RANKS.index('6')
    card_index = counter = 0 if trump_idx == 0 else trump_idx
    for card in cards[trump_idx:]:
        if highest_index > RANKS.index(card.rank):
            highest_index = RANKS.index(card.rank)
            card_index = counter
        counter += 1
    return card_index
