"""Player module"""
from card_deck_manager.exceptions.stack_exceptions import NotAStackError
from card_deck_manager.stack import TOP, Stack


class Player:
    """Represents a player"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: Stack = Stack(name=f"{self.name}'s hand")

    def __repr__(self) -> str:
        """Representation of the player object"""
        return f"<Player({self.name})>"

    def __str__(self) -> str:
        """Str cast of the player object"""
        return f"The player's name is {self.name}"

    def draw_card(self, target_stack: Stack, n: int = 1, add_position: str = TOP) -> None:
        """
        Draw n cards in a selected stack

        target_stack(Stack): stack in which the player draws
        n(int): number of cards to draw
        add_position(str): position to place the card in the player's stack
        """
        for _ in range(n):
            try:
                card = target_stack.pick_card()
            except AttributeError as e:
                raise NotAStackError from e
            self.hand.add_card(new_card=card, position=add_position)

    def play_card(self, target_stack: Stack, n: int = 1, play_position: str = TOP) -> None:
        """Play n cards from the player's hand to the target_stack"""
        if not isinstance(target_stack, Stack):
            raise NotAStackError
        for _ in range(n):
            card = self.hand.chose_card()
            target_stack.add_card(new_card=card, position=play_position)






