"""Testing Dealer."""
from card_deck_manager import D, H
from card_deck_manager.card import Card
from card_deck_manager.dealer import Dealer
from card_deck_manager.stack import Stack

c1 = Card(value="Q", suit=H)
c2 = Card(value="J", suit=D)
c3 = Card(value="Q", suit=D)
c4 = Card(value="5", suit=D)
s1 = Stack(name="Stack 1", cards=[c1, c2])
s2 = Stack(name="Stack 2", cards=[c3, c4])
s3 = Stack(name="Stack 3")
s_to_give = Stack(name="Stack to give", cards=[c1, c2, c3, c4])
dealer = Dealer(decks=[s1, s2])
dealer2 = Dealer(decks=[s_to_give])

def test_merge_all_decks() -> None:
    """Test merge_all_decks()."""
    dealer.merge_all_decks()
    decks_nb = 1
    assert len(dealer.decks) == decks_nb
    assert dealer.decks[0].cards == [c1, c2, c3, c4]

def test_give_card() -> None:
    """Test give_card()."""
    dealer2.give_card(deck=dealer2.decks[0], dest_stack=s3)
    assert dealer2.decks[0].cards == [c2, c3, c4]
    assert s3.cards == [c1]

def run_dealer_tests() -> None:
    """Run Dealer tests."""
    test_merge_all_decks()
    test_give_card()

if __name__ == "__main__":
    run_dealer_tests()
