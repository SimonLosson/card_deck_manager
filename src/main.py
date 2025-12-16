from card_deck_manager.card import Card
from card_deck_manager.stack import Stack, TOP, BOTTOM, RANDOM
from card_deck_manager import H, D, S, C

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="5", suit=S)
c4 = Card(value="A", suit=C)
c5 = Card(value="7", suit=S)


s = Stack(cards=[c1, c2, c3, c4])
print(s)
card = s.pick_card(position=RANDOM)
print(s)
print(card)






