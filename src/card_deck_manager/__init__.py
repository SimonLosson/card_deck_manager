"""Init card_deck_manager package."""
from card_deck_manager.deck_creation import classic_32_cards_deck_creation, classic_52_cards_deck_creation
from card_deck_manager.suit import C, D, H, S

__all__ = ["C", "D", "H", "S", "classic_32_cards_deck_creation", "classic_52_cards_deck_creation"]
