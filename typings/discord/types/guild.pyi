from .._typed_dict import NotRequired as NotRequired, Required as Required, TypedDict as TypedDict
from .activity import PartialPresenceUpdate as PartialPresenceUpdate
from .channel import GuildChannel as GuildChannel
from .emoji import Emoji as Emoji
from .member import Member as Member
from .role import Role as Role
from .scheduled_events import ScheduledEvent as ScheduledEvent
from .snowflake import Snowflake as Snowflake
from .threads import Thread as Thread
from .user import User as User
from .voice import GuildVoiceState as GuildVoiceState
from .welcome_screen import WelcomeScreen as WelcomeScreen
from _typeshed import Incomplete
from typing import Literal

class Ban(TypedDict):
    reason: str | None
    user: User

class UnavailableGuild(TypedDict):
    unavailable: NotRequired[bool]
    id: Snowflake

DefaultMessageNotificationLevel: Incomplete
ExplicitContentFilterLevel: Incomplete
MFALevel: Incomplete
VerificationLevel: Incomplete
NSFWLevel: Incomplete
PremiumTier: Incomplete
GuildFeature: Incomplete

class _BaseGuildPreview(UnavailableGuild):
    name: str
    icon: str | None
    splash: str | None
    discovery_splash: str | None
    emojis: list[Emoji]
    features: list[GuildFeature]
    description: str | None

class _GuildPreviewUnique(TypedDict):
    approximate_member_count: int
    approximate_presence_count: int

class GuildPreview(_BaseGuildPreview, _GuildPreviewUnique): ...

class Guild(_BaseGuildPreview):
    icon_hash: NotRequired[str | None]
    owner: NotRequired[bool]
    permissions: NotRequired[str]
    widget_enabled: NotRequired[bool]
    widget_channel_id: NotRequired[Snowflake | None]
    joined_at: NotRequired[str | None]
    large: NotRequired[bool]
    member_count: NotRequired[int]
    voice_states: NotRequired[list[GuildVoiceState]]
    members: NotRequired[list[Member]]
    channels: NotRequired[list[GuildChannel]]
    presences: NotRequired[list[PartialPresenceUpdate]]
    threads: NotRequired[list[Thread]]
    max_presences: NotRequired[int | None]
    max_members: NotRequired[int]
    premium_subscription_count: NotRequired[int]
    premium_progress_bar_enabled: NotRequired[bool]
    max_video_channel_users: NotRequired[int]
    guild_scheduled_events: NotRequired[list[ScheduledEvent]]
    owner_id: Snowflake
    afk_channel_id: Snowflake | None
    afk_timeout: int
    verification_level: VerificationLevel
    default_message_notifications: DefaultMessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: list[Role]
    mfa_level: MFALevel
    nsfw_level: NSFWLevel
    application_id: Snowflake | None
    system_channel_id: Snowflake | None
    system_channel_flags: int
    rules_channel_id: Snowflake | None
    vanity_url_code: str | None
    banner: str | None
    premium_tier: PremiumTier
    preferred_locale: str
    public_updates_channel_id: Snowflake | None

class InviteGuild(Guild, total=False):
    welcome_screen: WelcomeScreen

class GuildWithCounts(Guild, _GuildPreviewUnique): ...

class GuildPrune(TypedDict):
    pruned: int | None

class ChannelPositionUpdate(TypedDict):
    id: Snowflake
    position: int | None
    lock_permissions: bool | None
    parent_id: Snowflake | None

class RolePositionUpdate(TypedDict, total=False):
    id: Required[Snowflake]
    position: Snowflake | None

class GuildMFAModify(TypedDict):
    level: Literal[0, 1]

class GuildBulkBan(TypedDict):
    banned_users: list[Snowflake]
    failed_users: list[Snowflake]
