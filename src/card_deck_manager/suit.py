"""Suit module"""

from card_deck_manager.python_tools.singleton import Singleton

SUIT_MAP = {
    "heart": "♥",
    "diamond": "♦",
    "club": "♣",
    "spade": "♠",
}

class Suit:
    """Defines a suit"""

    def __init__(self, suit:str) -> None:
        self.suit = suit

    def __repr__(self) -> str:
        return SUIT_MAP[self.suit]

class Heart(Suit, metaclass=Singleton):
    """Singleton for heart suit"""

    def __init__(self):
        super().__init__(suit="heart")

class Diamond(Suit, metaclass=Singleton):
    """Singleton for diamond suit"""

    def __init__(self):
        super().__init__(suit="diamond")

class Club(Suit, metaclass=Singleton):
    """Singleton for club suit"""

    def __init__(self):
        super().__init__(suit="club")

class Spade(Suit, metaclass=Singleton):
    """Singleton for spade suit"""

    def __init__(self):
        super().__init__(suit="spade")

# Suits constants
H = Heart()
D = Diamond()
C = Club()
S = Spade()





