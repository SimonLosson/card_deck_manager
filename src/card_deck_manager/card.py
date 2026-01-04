"""Card module."""
from __future__ import annotations

from card_deck_manager.suit import Suit


class Card:
    """Represents a card."""

    def __init__(self, value:str, suit:Suit) -> None:
        """Init Card object."""
        self.value = value
        self.suit = suit
        self.is_head = None
        self.numeric_value = self._init_numeric_value()

    def __repr__(self) -> str:
        """Show value and suit of a card."""
        return f"< {self.value}{self.suit} >"

    def __eq__(self, other: Card) -> bool:
        """Check if two cards values are equal."""
        return self.value == other.value

    def __hash__(self) -> int:
        """Return a hash based on the card value."""
        return hash(self.value)

    def __lt__(self, other: Card) -> bool:
        """Check if card value is lower than other card value."""
        return self.value < other.value

    def __gt__(self, other: Card) -> bool:
        """Check if card value is greater than other card value."""
        return self.value > other.value

    def __le__(self, other: Card) -> bool:
        """Check if card value is lower or equal than other card value."""
        return self.value <= other.value

    def __ge__(self, other: Card) -> bool:
        """Check if card value is greater or equal than other card value."""
        return self.value >= other.value

    def _init_numeric_value(self) -> int:
        value_to_numeric_map = {
            "A": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
        }
        return value_to_numeric_map[self.value]
