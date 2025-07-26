from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete
from typing import TypedDict

class PartialUser(TypedDict):
    id: Snowflake
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None

PremiumType: Incomplete

class User(PartialUser, total=False):
    bot: bool
    system: bool
    mfa_enabled: bool
    local: str
    verified: bool
    email: str | None
    flags: int
    premium_type: PremiumType
    public_flags: int
