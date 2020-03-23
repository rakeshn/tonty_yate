from src.models.deck import Deck, Card
from src.models.game import Round

round = Round()
round.play(Card('Spades', '10'),'p1')
round.play(Card('Spades', '8'),'p2')
round.play(Card('Spades', 'Jack'),'p3')
round.play(Card('Spades', 'Ace'),'p4')
winner, score = round.end()
print("{0} won by {1}".format(winner, score))

# deck = Deck(4);
# deck.shuffle()
#
# #
# points = lambda rank: 3 if rank == 'Jack' else 2 if rank == '9' else 1 if rank == 'Ace' else 1 if rank == '10' else 0
# score = lambda cards: sum(points(card.rank) for card in cards)
#
#
# for i in range(deck.count):
#     # print(deck.cards[i])
#     x = deck.cards[i]
#     # print(x)
#     # print(points(x.rank))
# total = score(deck.cards)
# print(total)