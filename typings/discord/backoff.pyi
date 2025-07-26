from typing import Generic, Literal, TypeVar, overload

__all__ = ['ExponentialBackoff']

T = TypeVar('T', bool, Literal[True], Literal[False])

class ExponentialBackoff(Generic[T]):
    def __init__(self, base: int = 1, *, integral: T = False) -> None: ...
    @overload
    def delay(self) -> float: ...
    @overload
    def delay(self) -> int: ...
    @overload
    def delay(self) -> int | float: ...
