"""Stack module"""
from card_deck_manager.card import Card
from random import shuffle, randint
from card_deck_manager.exceptions.stack_exceptions import PositionError, NoSuchCardError

TOP = "TOP"
BOTTOM = "BOTTOM"
RANDOM = "RANDOM"


class Stack:
    """Represents a card stack"""

    def __init__(self, name: str, cards: list[Card] = None) -> None:
        self.name = name
        if cards is None:
            cards = []
        self.cards = cards

    def __repr__(self) -> str:
        """Representation of the stack object"""
        return f"| {self.name} : {self.cards} |"

    def shuffle(self) -> None:
        """Shuffle the stack cards"""
        shuffle(self.cards)
        print("Cards have been shuffled")

    def add_card(self, new_card: Card, position: str = TOP, index: int | None = None) -> None:
        """
        Add a card to the stack.

        If index is defined, position will be ignored.
        """
        if index is not None:
            self.cards.insert(index, new_card)
        else:
            match position:
                case "TOP":
                    self.cards.insert(0, new_card)
                case "BOTTOM":
                    self.cards.insert(len(self.cards), new_card)
                case "RANDOM":
                    rdm = randint(0, len(self.cards))
                    self.cards.insert(rdm, new_card)
                case _:
                    raise PositionError

    def pick_card(self, position: str = TOP, index: int | None = None) -> Card:
        """
        Pick one card

        If index is defined, position will be ignored
        """
        try:
            if index is not None:
                return self.cards.pop(index)
            match position:
                case "TOP":
                    return self.cards.pop(0)
                case "BOTTOM":
                    return self.cards.pop(len(self.cards) - 1)
                case "RANDOM":
                    rdm = randint(0, len(self.cards) - 1)
                    return self.cards.pop(rdm)
                case _:
                    raise PositionError
        except IndexError:
            raise NoSuchCardError()

    def chose_card(self) -> Card:
        """Show the card stack with cards positions and chose one card with its position"""
        for i, card in enumerate(self.cards):
            print(f"{i} : {card}")
        pos = int(input("Chose a card by its position : "))
        try:
            chosen_card = self.cards.pop(pos)
        except IndexError:
            raise NoSuchCardError()
        print(f"Chosen card : {chosen_card}")
        return chosen_card




