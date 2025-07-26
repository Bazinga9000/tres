from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .appinfo import PartialAppInfo as PartialAppInfo
from .channel import PartialChannel as PartialChannel
from .guild import InviteGuild as InviteGuild, _GuildPreviewUnique
from .scheduled_events import ScheduledEvent as ScheduledEvent
from .snowflake import Snowflake as Snowflake
from .user import PartialUser as PartialUser
from _typeshed import Incomplete

InviteTargetType: Incomplete

class _InviteMetadata(TypedDict, total=False):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str
    expires_at: str | None

class VanityInvite(_InviteMetadata):
    code: str | None

class IncompleteInvite(_InviteMetadata):
    code: str
    channel: PartialChannel

class Invite(IncompleteInvite):
    guild: NotRequired[InviteGuild]
    inviter: NotRequired[PartialUser]
    scheduled_event: NotRequired[ScheduledEvent]
    target_user: NotRequired[PartialUser]
    target_type: NotRequired[InviteTargetType]
    target_application: NotRequired[PartialAppInfo]

class InviteWithCounts(Invite, _GuildPreviewUnique): ...

class GatewayInviteCreate(TypedDict):
    guild_id: NotRequired[Snowflake]
    inviter: NotRequired[PartialUser]
    target_type: NotRequired[InviteTargetType]
    target_user: NotRequired[PartialUser]
    target_application: NotRequired[PartialAppInfo]
    channel_id: Snowflake
    code: str
    created_at: str
    max_age: int
    max_uses: int
    temporary: bool
    uses: bool

class GatewayInviteDelete(TypedDict):
    guild_id: NotRequired[Snowflake]
    channel_id: Snowflake
    code: str
GatewayInvite = GatewayInviteCreate | GatewayInviteDelete
