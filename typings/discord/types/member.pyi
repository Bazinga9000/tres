from .snowflake import SnowflakeList as SnowflakeList
from .user import User as User
from typing import TypedDict

class Nickname(TypedDict):
    nick: str

class PartialMember(TypedDict):
    roles: SnowflakeList
    joined_at: str
    deaf: bool
    mute: bool

class Member(PartialMember, total=False):
    avatar: str
    user: User
    nick: str
    premium_since: str
    pending: bool
    permissions: str
    communication_disabled_until: str
    flags: int

class _OptionalMemberWithUser(PartialMember, total=False):
    avatar: str
    nick: str
    premium_since: str
    pending: bool
    permissions: str

class MemberWithUser(_OptionalMemberWithUser):
    user: User

class UserWithMember(User, total=False):
    member: _OptionalMemberWithUser
