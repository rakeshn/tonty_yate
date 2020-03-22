import random

RANKS = ['Jack', '9', 'Ace', '10', 'King', 'Queen', '8', '7', '6']


class Card(object):
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck(object):
    def __init__(self, num_players: int):
        self.cards = []
        self.count = 0
        self.num_packs = 1

        if num_players == 4:
            self.count = 32

        elif num_players == 6:
            self.count = 48
            self.num_packs = 2
        else:
            raise Exception ("Number of players must be 4 or 6")

        cards_per_suit = int(self.count / 4 / self.num_packs)
        ranks_for_play = RANKS[:cards_per_suit]

        for i in range(self.num_packs):
            for rank in ranks_for_play:
                self.cards.append(Card('Spades', rank))
                self.cards.append(Card('Diamonds', rank))
                self.cards.append(Card('Hearts', rank))
                self.cards.append(Card('Clubs', rank))

    def shuffle(self):
        mid = int(len(self.cards) / 2)

        for i in range(mid):
            r = random.randrange(mid)
            self.cards[-i], self.cards[r] = self.cards[r], self.cards[-i]
