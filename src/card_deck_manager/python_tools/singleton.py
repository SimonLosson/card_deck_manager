"""Defines singleton implementation"""
class Singleton(type):
    """Singleton class"""

    _instances = {}  # noqa: RUF012
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
