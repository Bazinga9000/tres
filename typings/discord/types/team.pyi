from .snowflake import Snowflake as Snowflake
from .user import PartialUser as PartialUser
from typing import TypedDict

class TeamMember(TypedDict):
    user: PartialUser
    membership_state: int
    permissions: list[str]
    team_id: Snowflake

class Team(TypedDict):
    id: Snowflake
    name: str
    owner_id: Snowflake
    members: list[TeamMember]
    icon: str | None
