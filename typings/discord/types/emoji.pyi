from .snowflake import Snowflake as Snowflake, SnowflakeList as SnowflakeList
from .user import User as User
from typing import TypedDict

class PartialEmoji(TypedDict):
    id: Snowflake | None
    name: str | None

class Emoji(PartialEmoji, total=False):
    roles: SnowflakeList
    user: User
    require_colons: bool
    managed: bool
    animated: bool
    available: bool

class EditEmoji(TypedDict):
    name: str
    roles: SnowflakeList | None
