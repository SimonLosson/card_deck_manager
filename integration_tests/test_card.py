"""Testing Card."""
from card_deck_manager import D, H
from card_deck_manager.card import Card

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="Q", suit=D)
c4 = Card(value="5", suit=D)

def test_cards() -> None:
    """Test cards."""
    queen_numeric_value = 12
    assert c1.numeric_value == queen_numeric_value
    assert c1.suit == H
    assert c1.value == "Q"

def test_compare_cards() -> None:
    """Test cards comparisons."""
    assert c1 > c2
    assert c1 >= c3
    assert c2 < c1
    assert c3 <= c1
    assert not c1 == c2  # noqa: SIM201
    assert c1 != c2

def test_card_repr() -> None:
    """Test card representation."""
    assert c1.__repr__() == "< Q♥ >"

def test_is_head() -> None:
    """Test is_head()."""
    assert c1.is_head()
    assert not c4.is_head()

def run_card_tests() -> None:
    """Run Card tests."""
    test_cards()
    test_compare_cards()
    test_card_repr()
    test_is_head()

if __name__ == "__main__":
    run_card_tests()
