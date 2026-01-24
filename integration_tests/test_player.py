"""Testing Player."""
from unittest.mock import patch

from card_deck_manager import D, H
from card_deck_manager.card import Card
from card_deck_manager.player import Player
from card_deck_manager.stack import Stack

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="Q", suit=D)
c4 = Card(value="5", suit=D)
s1 = Stack(name="Stack 1", cards=[c1, c2])
s2 = Stack(name="Stack 2", cards=[c3, c4])
s3 = Stack(name="Stack 3", cards=[c3, c4])
s4 = Stack(name="Stack 4")
player1 = Player(name="A", stack_names=["Hand"])
player1.stacks[0] = s1
player2 = Player(name="B", stack_names=["Hand"])
player2.hand = Stack(name="B's hand", cards=[c3, c4])


def test_player_representation() -> None:
    """Test Player representation."""
    assert player1.__repr__() == f"<Player({player1.name})>"

def test_player_str() -> None:
    """Test Player cast to str."""
    assert str(player1) == f"The player's name is {player1.name}"

def test_draw_card() -> None:
    """Test draw_card()."""
    player1.draw_card(s3)
    assert player1.stacks[0].cards[0] == c3
    assert s3.cards == [c4]

@patch("builtins.input", lambda _: 0)
def test_play_card() -> None:
    """Test play_card()."""
    player2.play_card(s4)
    assert player2.hand.cards == [c4]
    assert s4.cards == [c3]

def run_player_tests() -> None:
    """Run Player tests."""
    test_player_representation()
    test_player_str()
    test_draw_card()
    test_play_card()

if __name__ == "__main__":
    run_player_tests()

