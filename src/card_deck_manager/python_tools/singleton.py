"""Defines singleton implementation."""
from typing import Any, TypeVar

T = TypeVar("T")

class Singleton(type):
    """Singleton class."""

    _instances = {}  # noqa: RUF012
    def __call__(cls: type[T], *args: Any, **kwargs: Any) -> T:  # noqa: ANN401
        """Singleton implementation."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
