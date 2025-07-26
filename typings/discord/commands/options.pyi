from ..abc import GuildChannel, Mentionable
from ..channel import Thread
from ..enums import ChannelType, Enum as DiscordEnum, SlashCommandOptionType
from ..ext.commands import Converter
from ..member import Member
from ..message import Attachment
from ..role import Role
from ..user import User
from _typeshed import Incomplete
from enum import Enum
from typing import Literal

__all__ = ['ThreadOption', 'Option', 'OptionChoice', 'option']

InputType = type[str] | type[bool] | type[int] | type[float] | type[GuildChannel] | type[Thread] | type[Member] | type[User] | type[Attachment] | type[Role] | type[Mentionable] | SlashCommandOptionType | Converter | type[Converter] | type[Enum] | type[DiscordEnum]

class ThreadOption:
    def __init__(self, thread_type: Literal['public', 'private', 'news']) -> None: ...

class Option:
    input_type: SlashCommandOptionType
    converter: Converter | type[Converter] | None
    name: str | None
    description: Incomplete
    channel_types: list[ChannelType]
    required: bool
    default: Incomplete
    autocomplete: Incomplete
    choices: list[OptionChoice]
    min_value: int | float | None
    max_value: int | float | None
    min_length: int | None
    max_length: int | None
    name_localizations: Incomplete
    description_localizations: Incomplete
    def __init__(self, input_type: InputType = ..., /, description: str | None = None, **kwargs) -> None: ...
    def to_dict(self) -> dict: ...

class OptionChoice:
    name: Incomplete
    value: Incomplete
    name_localizations: Incomplete
    def __init__(self, name: str, value: str | int | float | None = None, name_localizations: dict[str, str] = ...) -> None: ...
    def to_dict(self) -> dict[str, str | int | float]: ...

def option(name, input_type=None, **kwargs): ...
