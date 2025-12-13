from suit import Suit
from card import Card

s = Suit(suit="heart")
c = Card(value="Q", suit=s)

print(c)