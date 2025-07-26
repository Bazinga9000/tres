import datetime
from .mixins import Hashable
from _typeshed import Incomplete
from typing import SupportsInt

__all__ = ['Object']

SupportsIntCast = SupportsInt | str | bytes | bytearray

class Object(Hashable):
    id: Incomplete
    def __init__(self, id: SupportsIntCast) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def worker_id(self) -> int: ...
    @property
    def process_id(self) -> int: ...
    @property
    def increment_id(self) -> int: ...
