from typing import Callable

from .base import BaseSelect


class TypedSelect[T](BaseSelect):
    def __init__(self, converter: Callable[[str], T]):
        super().__init__()
        self.converter = converter
    
    def get_value(self) -> T:
        return self.converter(self.get_raw_value())
