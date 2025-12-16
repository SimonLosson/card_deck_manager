from card_deck_manager.card import Card
from card_deck_manager.player import Player
from card_deck_manager.stack import Stack, TOP, BOTTOM, RANDOM
from card_deck_manager import H, D, S, C

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="5", suit=S)
c4 = Card(value="A", suit=C)
c5 = Card(value="7", suit=S)


s = Stack(cards=[c1, c2, c3, c4], name="Draw")
print(s)


player1 = Player("Simon")
print(player1.hand)
player1.draw_card(target_stack=s, n=2)

print(s)
print(player1.hand)

print(str(player1))

player1.play_card(s)


print(s)




