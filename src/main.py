from card_deck_manager.card import Card
from card_deck_manager.player import Player
from card_deck_manager.stack import Stack, TOP, BOTTOM, RANDOM
from card_deck_manager import (
    H,
    D,
    S,
    C,
    classic_52_cards_deck_creation,
    classic_32_cards_deck_creation,
)
from card_deck_manager.game import Game, ConcreteGame
from card_deck_manager.deck_creation import classic_52_cards_deck_creation, classic_32_cards_deck_creation
from card_deck_manager.dealer import Dealer

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="5", suit=S)
c4 = Card(value="A", suit=C)
c5 = Card(value="7", suit=S)

s1 = Stack(cards=[c1, c2], name="s1")
s2 = Stack(cards=[c3, c4], name="s2")



# print(t)
# print(s)
#
#
player1 = Player("Simon")
# print(player1.hand)
# player1.draw_card(target_stack=s, n=2)
#
# print(s)
# print(player1.hand)
#
# print(str(player1))
#
# player1.play_card(s)
#
#
# print(s)

game = ConcreteGame(players=[player1], initial_decks_cards=[s1.cards, s2.cards])
for deck in game.dealer.decks:
    print(deck)
test = game.dealer.merge_all_decks()
print(test)
print(game.dealer.decks)




