from src.models.deck import Deck, Card
from src.models.game import Round, Game

# main class for temporary testing


# Basic test:  First player with highest card should win
game = Game()
round = Round(game)
round.play(Card('Spades', 'Jack'),'p1')  # Winner
round.play(Card('Spades', 'Jack'),'p2')
round.play(Card('Spades', '7'),'p3')
round.play(Card('Spades', 'Jack'),'p4')
winner, score = round.end()
print("Test#1 :: {0} won by {1}".format(winner, score))


# Trump test:  player with trump should win. Assuming trump was called in previous game
game = Game()
game.call_trump()
game.trump = Card('Hearts', '6')
round = Round(game)
round.play(Card('Spades', 'Jack'),'p1')
round.play(Card('Spades', 'Jack'),'p2')
round.play(Card('Hearts', '6'),'p3')  # Winner
round.play(Card('Spades', 'Jack'),'p4')
winner, score = round.end()
print("Test#2 :: {0} won by {1}".format(winner, score))


# Trump test:  player with trump should win. Assuming trump was called before the play
game = Game()
game.trump = Card('Hearts', '6')
round = Round(game)
round.play(Card('Spades', 'Jack'),'p1')
round.play(Card('Spades', 'Jack'),'p2')
round.call_trump()
round.play(Card('Hearts', '6'),'p3')  # Winner
round.play(Card('Spades', 'Jack'),'p4')
winner, score = round.end()
print("Test#3 :: {0} won by {1}".format(winner, score))

# Trump test:  player with trump should win. Assuming no one played trump after calling in current round
game = Game()
game.trump = Card('Hearts', '6')
round = Round(game)
round.play(Card('Spades', 'Jack'),'p1')  # Winner
round.play(Card('Spades', 'Jack'),'p2')
round.play(Card('Hearts', '6'),'p3')
round.call_trump()
round.play(Card('Spades', 'Jack'),'p4')
winner, score = round.end()
print("Test#4 :: {0} won by {1}".format(winner, score))


# Trump test: Trump called in first game. Trump was used only in next round(s)
game = Game()
game.trump = Card('Hearts', '6')
round = Round(game)
round.play(Card('Spades', 'Jack'),'p1')  # Winner
round.play(Card('Spades', 'Jack'),'p2')
round.play(Card('Hearts', '6'),'p3')
round.call_trump()
round.play(Card('Spades', 'Jack'),'p4')
winner, score = round.end()
print("Test#5a :: {0} won by {1}".format(winner, score))

round = Round(game)
round.play(Card('Diamonds', 'Jack'),'p1')
round.play(Card('Hearts', '7'),'p2')  # Winner
round.play(Card('Diamonds', '6'),'p3')
round.play(Card('Diamonds', 'Jack'),'p4')
winner, score = round.end()
print("Test#5b :: {0} won by {1}".format(winner, score))