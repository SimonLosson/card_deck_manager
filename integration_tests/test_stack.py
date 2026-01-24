"""Testing Stack."""
from unittest.mock import patch

from card_deck_manager import D, H
from card_deck_manager.card import Card
from card_deck_manager.stack import Stack

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="Q", suit=D)
c4 = Card(value="5", suit=D)
s1 = Stack(name="Stack 1", cards=[c1, c2])
s2 = Stack(name="Stack 2", cards=[c3, c4])
s3 = Stack(name="Stack 3")
shuffle_s = Stack(name="Stack to shuffle", cards=[c1, c2, c3, c4])

def test_stack_repr() -> None:
    """Test stack representation."""
    assert s1.__repr__() == f"| Stack 1 : {s1.cards} |"

def test_stack_add() -> None:
    """Test stack addtion."""
    tmp_s = s1 + s2
    assert tmp_s.name == s1.name
    assert [*tmp_s.cards] == [*s1.cards, *s2.cards]

def test_len() -> None:
    """Test stack len()."""
    assert len(s1) == len(s1.cards)
    assert len(s3) == 0

def test_shuffle() -> None:
    """Test shuffle()."""
    tmp_cards = shuffle_s.cards.copy()
    for _ in range(1000):
        shuffle_s.shuffle()
        if tmp_cards != shuffle_s.cards:
            return
    raise ValueError("Cards order didn't change after 1000 loops")  # noqa: EM101, TRY003

def test_add_cards() -> None:
    """Test add_cards()."""
    tmp_cards = s1.cards.copy()
    s1.add_cards([c3, c4])
    assert s1.cards == [c4, c3, *tmp_cards]

def test_empty() -> None:
    """Test empty()."""
    tmp_cards = s2.cards.copy()
    assert s2.empty() == [*tmp_cards]
    assert not s2.cards

def test_pick_card() -> None:
    """Test pick_card()."""
    tmp_cards = s1.cards.copy()
    assert s1.pick_card() == tmp_cards[0]
    tmp_cards.pop(0)
    assert s1.cards == tmp_cards

@patch("builtins.input", lambda _: 0)
def test_chose_card() -> None:
    """Test chose_card()."""
    tmp_cards = s1.cards.copy()
    assert s1.chose_card() == tmp_cards[0]
    tmp_cards.pop(0)
    assert s1.cards == tmp_cards

def run_stack_tests() -> None:
    """Run Stack tests."""
    test_stack_repr()
    test_stack_add()
    test_len()
    test_shuffle()
    test_add_cards()
    test_empty()
    test_pick_card()
    test_chose_card()

if __name__ == "__main__":
    run_stack_tests()



