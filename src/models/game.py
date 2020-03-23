import uuid

from models.deck import RANKS
from models import deck


class Player:
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4().hex)
        self.cards = []

class Game:
    def __init__(self):
        self.players = []
        self.id = str(uuid.uuid4().hex)
        self.deck = []
        self.trump = None
        self.trump_called = False
        self.started = False

    def not_allowed_if_game_started(self, action: str):
        if self.started:
            raise Exception(f'{action} is not allowed as the game has started.')

    def register_player(self, name: str):
        self.not_allowed_if_game_started('Add player')
        player = Player(name)
        self.players.append(player)
        return player.id

    def start_game(self):
        self.deck = deck.Deck(len(self.players))
        self.deck.shuffle()
        self.started = True
        self.deal()

    def deal(self):
        num_players = len(self.players)
        if len(self.deck) % num_players != 0:
            raise Exception('Not enough cards to deal')
        for player in self.players:
            player.cards = self.deck[:4]
            self.deck = self.deck[:4]

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



