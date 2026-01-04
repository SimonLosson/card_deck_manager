"""Game module."""
import abc

from card_deck_manager import classic_52_cards_deck_creation
from card_deck_manager.card import Card
from card_deck_manager.dealer import Dealer
from card_deck_manager.player import Player
from card_deck_manager.stack import Stack


class Game(metaclass=abc.ABCMeta):
    """Represents an abstract game."""

    def __init__(self, players: list[Player], initial_decks_cards: list[list[Card]] | None = None) -> None:
        """Init abstract class Game."""
        if initial_decks_cards is None:
            initial_decks_cards: list[list[Card]] = [classic_52_cards_deck_creation()]
        self.players = players
        self.initial_decks_cards = initial_decks_cards
        self.initial_decks = self.create_decks()
        self.piles: dict[str, Stack] = {}
        self.dealer: Dealer = Dealer(decks=self.initial_decks)

    def create_decks(self) -> list[Stack]:
        """Create a deck of cards."""
        return [
            Stack(name=f"Deck {i + 1}", cards=initial_deck_cards)
            for i, initial_deck_cards in enumerate(self.initial_decks_cards)
        ]

    @abc.abstractmethod
    def run(self) -> None:
        """Run abstract method."""
        return

class ConcreteGame(Game):
    """Represents a concrete game."""

    def __init__(self, players: list[Player], initial_decks_cards: list[list[Card]] | None = None) -> None:
        """Init ConcreteGame object."""
        super().__init__(players=players, initial_decks_cards=initial_decks_cards)

    def run(self) -> None:
        """Keep the game running."""
        print("Game is running !")
