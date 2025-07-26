from .abc import Snowflake
from .emoji import Emoji
from .guild import Guild
from .partial_emoji import PartialEmoji
from .types.welcome_screen import WelcomeScreen as WelcomeScreenPayload, WelcomeScreenChannel as WelcomeScreenChannelPayload
from _typeshed import Incomplete
from typing import overload

__all__ = ['WelcomeScreen', 'WelcomeScreenChannel']

class WelcomeScreenChannel:
    channel: Incomplete
    description: Incomplete
    emoji: Incomplete
    def __init__(self, channel: Snowflake, description: str, emoji: Emoji | PartialEmoji | str) -> None: ...
    def to_dict(self) -> WelcomeScreenChannelPayload: ...

class WelcomeScreen:
    def __init__(self, data: WelcomeScreenPayload, guild: Guild) -> None: ...
    @property
    def enabled(self) -> bool: ...
    @property
    def guild(self) -> Guild: ...
    @overload
    async def edit(self, *, description: str | None = ..., welcome_channels: list[WelcomeScreenChannel] | None = ..., enabled: bool | None = ..., reason: str | None = ...) -> None: ...
    @overload
    async def edit(self) -> None: ...
