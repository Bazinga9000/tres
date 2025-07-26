from .abc import Snowflake
from .types.message import AllowedMentions as AllowedMentionsPayload
from _typeshed import Incomplete
from typing import TypeVar

__all__ = ['AllowedMentions']

class _FakeBool:
    def __eq__(self, other): ...
    def __bool__(self) -> bool: ...
A = TypeVar('A', bound='AllowedMentions')

class AllowedMentions:
    everyone: Incomplete
    users: Incomplete
    roles: Incomplete
    replied_user: Incomplete
    def __init__(self, *, everyone: bool = ..., users: bool | list[Snowflake] = ..., roles: bool | list[Snowflake] = ..., replied_user: bool = ...) -> None: ...
    @classmethod
    def all(cls) -> A: ...
    @classmethod
    def none(cls) -> A: ...
    def to_dict(self) -> AllowedMentionsPayload: ...
    def merge(self, other: AllowedMentions) -> AllowedMentions: ...
