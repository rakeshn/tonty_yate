from src.models.deck import Deck, Card
from src.models.game import Round

# main class for temporary testing

round = Round()
round.play(Card('Spades', '10'),'p1')
round.play(Card('Spades', '8'),'p2')
round.play(Card('Spades', '7'),'p3')
round.play(Card('Spades', 'Ace'),'p4')
winner, score = round.end()
print("{0} won by {1}".format(winner, score))