from .asset import Asset
from .enums import TeamMembershipState
from .state import ConnectionState
from .types.team import Team as TeamPayload, TeamMember as TeamMemberPayload
from .user import BaseUser

__all__ = ['Team', 'TeamMember']

class Team:
    id: int
    name: str
    owner_id: int | None
    members: list[TeamMember]
    def __init__(self, state: ConnectionState, data: TeamPayload) -> None: ...
    @property
    def icon(self) -> Asset | None: ...
    @property
    def owner(self) -> TeamMember | None: ...

class TeamMember(BaseUser):
    team: Team
    membership_state: TeamMembershipState
    permissions: list[str]
    def __init__(self, team: Team, state: ConnectionState, data: TeamMemberPayload) -> None: ...
