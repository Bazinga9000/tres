from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from ..enums import SortOrder as SortOrder
from ..flags import ChannelFlags as ChannelFlags
from .snowflake import Snowflake as Snowflake
from .threads import ThreadArchiveDuration as ThreadArchiveDuration, ThreadMember as ThreadMember, ThreadMetadata as ThreadMetadata
from .user import User as User
from _typeshed import Incomplete
from typing import Literal

OverwriteType: Incomplete

class PermissionOverwrite(TypedDict):
    id: Snowflake
    type: OverwriteType
    allow: str
    deny: str

ChannelType: Incomplete

class _BaseChannel(TypedDict):
    id: Snowflake
    name: str

class _BaseGuildChannel(_BaseChannel):
    guild_id: Snowflake
    position: int
    permission_overwrites: list[PermissionOverwrite]
    nsfw: bool
    parent_id: Snowflake | None

class PartialChannel(_BaseChannel):
    type: ChannelType

class _TextChannelOptional(TypedDict, total=False):
    topic: str
    last_message_id: Snowflake | None
    last_pin_timestamp: str
    rate_limit_per_user: int
    default_auto_archive_duration: ThreadArchiveDuration
    default_thread_rate_limit_per_user: int

class TextChannel(_BaseGuildChannel, _TextChannelOptional):
    type: Literal[0]

class DefaultReaction(TypedDict):
    emoji_id: NotRequired[Snowflake | None]
    emoji_name: NotRequired[str | None]

class ForumTag(TypedDict):
    id: Snowflake
    name: str
    moderated: bool
    emoji_id: NotRequired[Snowflake | None]
    emoji_name: NotRequired[str | None]

class ForumChannel(_BaseGuildChannel, _TextChannelOptional):
    type: Literal[15]
    available_tags: NotRequired[list[ForumTag] | None]
    default_reaction_emoji: NotRequired[DefaultReaction | None]
    default_sort_order: NotRequired[SortOrder | None]
    flags: ChannelFlags

class NewsChannel(_BaseGuildChannel, _TextChannelOptional):
    type: Literal[5]

VideoQualityMode: Incomplete

class VoiceChannel(_BaseGuildChannel):
    rtc_region: NotRequired[str | None]
    video_quality_mode: NotRequired[VideoQualityMode]
    status: NotRequired[str | None]
    type: Literal[2]
    bitrate: int
    user_limit: int

class CategoryChannel(_BaseGuildChannel):
    type: Literal[4]

class StageChannel(_BaseGuildChannel):
    rtc_region: NotRequired[str | None]
    topic: NotRequired[str]
    type: Literal[13]
    bitrate: int
    user_limit: int

class ThreadChannel(_BaseChannel):
    member: NotRequired[ThreadMember]
    owner_id: NotRequired[Snowflake]
    rate_limit_per_user: NotRequired[int]
    last_message_id: NotRequired[Snowflake | None]
    last_pin_timestamp: NotRequired[str]
    type: Literal[10, 11, 12]
    guild_id: Snowflake
    parent_id: Snowflake
    nsfw: bool
    message_count: int
    member_count: int
    thread_metadata: ThreadMetadata
    applied_tags: NotRequired[list[Snowflake] | None]
    flags: ChannelFlags
    total_message_sent: int
GuildChannel = TextChannel | NewsChannel | VoiceChannel | CategoryChannel | StageChannel | ThreadChannel | ForumChannel

class DMChannel(TypedDict):
    id: Snowflake
    type: Literal[1]
    last_message_id: Snowflake | None
    recipients: list[User]

class GroupDMChannel(_BaseChannel):
    type: Literal[3]
    icon: str | None
    owner_id: Snowflake
Channel = GuildChannel | DMChannel | GroupDMChannel
PrivacyLevel: Incomplete

class StageInstance(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: PrivacyLevel
    discoverable_disabled: bool
    guild_scheduled_event_id: Snowflake
