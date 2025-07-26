import datetime
from .abc import GuildChannel
from .appinfo import PartialAppInfo
from .asset import Asset
from .enums import ChannelType, InviteTarget, VerificationLevel
from .guild import Guild
from .mixins import Hashable
from .scheduled_events import ScheduledEvent
from .state import ConnectionState
from .types.channel import PartialChannel as InviteChannelPayload
from .types.invite import GatewayInvite as GatewayInvitePayload, Invite as InvitePayload, InviteGuild as InviteGuildPayload, VanityInvite as VanityInvitePayload
from .user import User
from typing import TypeVar

__all__ = ['PartialInviteChannel', 'PartialInviteGuild', 'Invite']

class PartialInviteChannel:
    id: int
    name: str
    type: ChannelType
    def __init__(self, data: InviteChannelPayload) -> None: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class PartialInviteGuild:
    id: int
    name: str
    features: list[str]
    verification_level: VerificationLevel
    description: str | None
    def __init__(self, state: ConnectionState, data: InviteGuildPayload, id: int) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def icon(self) -> Asset | None: ...
    @property
    def banner(self) -> Asset | None: ...
    @property
    def splash(self) -> Asset | None: ...
I = TypeVar('I', bound='Invite')

class Invite(Hashable):
    BASE: str
    max_age: int | None
    code: str
    guild: InviteGuildType | None
    revoked: bool | None
    created_at: datetime.datetime | None
    temporary: bool | None
    uses: int | None
    max_uses: int | None
    approximate_presence_count: int | None
    approximate_member_count: int | None
    expires_at: datetime.datetime | None
    inviter: User | None
    channel: InviteChannelType | None
    target_user: User | None
    target_type: InviteTarget
    scheduled_event: ScheduledEvent | None
    target_application: PartialAppInfo | None
    def __init__(self, *, state: ConnectionState, data: InvitePayload | VanityInvitePayload, guild: PartialInviteGuild | Guild | None = None, channel: PartialInviteChannel | GuildChannel | None = None) -> None: ...
    @classmethod
    def from_incomplete(cls, *, state: ConnectionState, data: InvitePayload) -> I: ...
    @classmethod
    def from_gateway(cls, *, state: ConnectionState, data: GatewayInvitePayload) -> I: ...
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str: ...
    @property
    def url(self) -> str: ...
    async def delete(self, *, reason: str | None = None): ...
    def set_scheduled_event(self, event: ScheduledEvent) -> None: ...
