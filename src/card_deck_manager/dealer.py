#TODO : dealer initiates by giving cards to the player's hands
"""Dealer module"""
from card_deck_manager.player import Player
from card_deck_manager.stack import Stack, TOP


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

    @staticmethod
    def give_card(
            deck: Stack,
            player: Player,
            origin_position: str = TOP,
            origin_index: int | None = None,
            destination_position: str = TOP,
            destination_index: int | None = None,
    ) -> None:
        """Takes one card from one deck and gives it to one player"""
        given_card = deck.pick_card(position=origin_position, index=origin_index)
        player.hand.add_card(new_card=given_card, position=destination_position, index=destination_index)





