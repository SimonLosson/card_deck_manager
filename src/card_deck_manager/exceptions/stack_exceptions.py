class PositionError(Exception):
    """Error for illegal position of a card in a deck"""

class NoSuchCardError(Exception):
    """Error if chosen index isn't in the card stack range"""
