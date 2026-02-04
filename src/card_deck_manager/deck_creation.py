"""Module which contains functions to create card decks."""
from collections.abc import Callable

from card_deck_manager.card import Card
from card_deck_manager.suit import C, D, H, S

CLASSIC_CARDS_VALUES_52_CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CLASSIC_CARDS_VALUES_32_CARDS = ["A", "7", "8", "9", "10", "J", "Q", "K"]
CLASSIC_CARDS_SUITS = [H, D, C, S]


def classic_52_cards_deck_creation(
        card_callable: Callable = Card,
        numeric_value_callable: Callable | None = None,
) -> list[Card]:
    """Create a classic 52 card deck."""
    return [
        card_callable(value=value, suit=suit, numeric_value_callable=numeric_value_callable)
        for suit in CLASSIC_CARDS_SUITS
        for value in CLASSIC_CARDS_VALUES_52_CARDS
    ]


def classic_32_cards_deck_creation(card_callable: Callable = Card,
                                   numeric_value_callable: Callable | None = None,
                                   ) -> list[Card]:
    """Create a classic 52 card deck."""
    return [
        card_callable(value=value, suit=suit, numeric_value_callable=numeric_value_callable)
        for suit in CLASSIC_CARDS_SUITS
        for value in CLASSIC_CARDS_VALUES_32_CARDS
    ]

def deck_factory(
        deck_callable: Callable = classic_52_cards_deck_creation,
        card_callable: Callable = Card,
        numeric_value_callable: Callable | None = None,
) -> list[Card]:
    """Deck factory."""
    return deck_callable(card_callable, numeric_value_callable)
