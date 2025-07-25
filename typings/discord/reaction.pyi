from .abc import Snowflake
from .colour import Colour
from .emoji import Emoji
from .enums import ReactionType
from .iterators import ReactionIterator
from .message import Message
from .partial_emoji import PartialEmoji
from .types.message import Reaction as ReactionPayload, ReactionCountDetails as ReactionCountDetailsPayload
from _typeshed import Incomplete
from typing import Any

__all__ = ['Reaction', 'ReactionCountDetails']

class Reaction:
    message: Message
    emoji: PartialEmoji | Emoji | str
    count: int
    me: bool
    burst: bool
    me_burst: bool
    def __init__(self, *, message: Message, data: ReactionPayload, emoji: PartialEmoji | Emoji | str | None = None) -> None: ...
    @property
    def burst_colours(self) -> list[Colour]: ...
    @property
    def burst_colors(self) -> list[Colour]: ...
    @property
    def count_details(self): ...
    def is_custom_emoji(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    async def remove(self, user: Snowflake) -> None: ...
    async def clear(self) -> None: ...
    def users(self, *, limit: int | None = None, after: Snowflake | None = None, type: ReactionType | None = None) -> ReactionIterator: ...

class ReactionCountDetails:
    normal: Incomplete
    burst: Incomplete
    def __init__(self, data: ReactionCountDetailsPayload) -> None: ...
