from .base import BaseSelect

from typeutils import F


class TypedSelect[T](BaseSelect):
    def __init__(self, converter: F[[str], T]):
        super().__init__()
        self.converter = converter
    
    def get_value(self) -> T:
        return self.converter(self.get_raw_value())
