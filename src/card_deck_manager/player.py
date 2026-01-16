"""Player module."""
from card_deck_manager.exceptions.stack_exceptions import NotAStackError
from card_deck_manager.stack import TOP, Stack


class Player:
    """Represents a player."""

    def __init__(self, name: str, stack_names: list[str] | None = None) -> None:
        """Init Player object."""
        if stack_names is None:
            stack_names = []
        self.name = name
        self.hand: Stack = Stack(name=f"{self.name}'s hand")
        self.stacks = {stack_name : Stack(stack_name) for stack_name in stack_names}

    def __repr__(self) -> str:
        """Representation of the player object."""
        return f"<Player({self.name})>"

    def __str__(self) -> str:
        """Str cast of the player object."""
        return f"The player's name is {self.name}"

    def draw_card(
            self,
            origin_stack: Stack,
            dest_stack: Stack | None = None,
            n: int = 1,
            origin_position: str = TOP,
            dest_position: str = TOP) -> None:
        """
        Draw n cards in a selected stack.

        origin_stack(Stack): stack in which the player draws,
        dest_stack(Stack): stack in which the card is added (default is self.hand),
        n(int): number of cards to draw,
        dest_position(str): position to place the card in the dest stack.
        """
        if dest_stack is None:
            dest_stack = self.hand
        for _ in range(n):
            try:
                card = origin_stack.pick_card(position=origin_position)
            except AttributeError as e:
                raise NotAStackError from e
            dest_stack.add_card(new_card=card, position=dest_position)

    def play_card(self, dest_stack: Stack, n: int = 1, play_position: str = TOP) -> None:
        """Play n cards from the player's hand to the dest_stack."""
        if not isinstance(dest_stack, Stack):
            raise NotAStackError
        for _ in range(n):
            card = self.hand.chose_card()
            dest_stack.add_card(new_card=card, position=play_position)
