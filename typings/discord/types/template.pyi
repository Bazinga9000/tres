from .guild import Guild as Guild
from .snowflake import Snowflake as Snowflake
from .user import User as User
from typing import TypedDict

class CreateTemplate(TypedDict):
    name: str
    icon: bytes | None

class Template(TypedDict):
    code: str
    name: str
    description: str | None
    usage_count: int
    creator_id: Snowflake
    creator: User
    created_at: str
    updated_at: str
    source_guild_id: Snowflake
    serialized_source_guild: Guild
    is_dirty: bool | None
