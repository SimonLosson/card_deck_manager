"""Suit module"""
SUIT_MAP = {
    "heart": "♥",
    "diamond": "♦",
    "club": "♣",
    "spade": "♠",
}

class Suit:
    """Defines a suit"""
    def __init__(self, suit:str):
        self.suit = suit

    def __repr__(self):
        return SUIT_MAP[self.suit]




