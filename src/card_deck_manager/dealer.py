#TODO : dealer initiates by giving cards to the player's hands
"""Dealer module"""
from card_deck_manager.stack import Stack


class Dealer:
    """Represents a dealer"""

    def __init__(self, decks: list[Stack]) -> None:
        self.decks = decks

    def merge_all_decks(self) -> Stack:
        """Takes all decks and merge them to return a single deck"""
        for deck in self.decks[1:]:
            self.decks[0] += deck
        self.decks = [self.decks[0]]
        return self.decks[0]






