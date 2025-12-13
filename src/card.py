"""Card module"""
from suit import Suit

class Card:
    """Represents a card"""
    def __init__(self, value:str, suit:Suit):
        self.value = value
        self.suit = suit
        self.is_head = None
        self.numeric_value = self._init_numeric_value()

    def __repr__(self):
        return f"< {self.value}{self.suit} >"

    def _init_numeric_value(self):
        value_to_numeric_map = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "10",
            "J": "11",
            "Q": "12",
            "K": "13",
        }

        return value_to_numeric_map[self.numeric_value]
