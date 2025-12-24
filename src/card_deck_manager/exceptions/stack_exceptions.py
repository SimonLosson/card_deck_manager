"""Stack exceptions."""

class PositionError(Exception):
    """Error for illegal position of a card in a deck"""

class NoSuchCardError(Exception):
    """Error if chosen index isn't in the card stack range"""

class NotAStackError(Exception):
    """Error if object isn't a stack"""

