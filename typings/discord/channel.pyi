import datetime
import discord.abc
from .abc import Snowflake, SnowflakeTime
from .asset import Asset
from .emoji import Emoji
from .enums import ChannelType, EmbeddedActivity, SortOrder, StagePrivacyLevel, VideoQualityMode, VoiceRegion
from .guild import Guild, GuildChannel as GuildChannelType
from .invite import Invite
from .iterators import ArchivedThreadIterator
from .member import Member, VoiceState
from .message import EmojiInputType, Message, PartialMessage
from .mixins import Hashable
from .partial_emoji import PartialEmoji
from .permissions import PermissionOverwrite, Permissions
from .role import Role
from .stage_instance import StageInstance
from .state import ConnectionState
from .threads import Thread
from .types.channel import CategoryChannel as CategoryChannelPayload, DMChannel as DMChannelPayload, ForumChannel as ForumChannelPayload, ForumTag as ForumTagPayload, GroupDMChannel as GroupChannelPayload, StageChannel as StageChannelPayload, TextChannel as TextChannelPayload, VoiceChannel as VoiceChannelPayload
from .types.threads import ThreadArchiveDuration
from .user import ClientUser, User
from .webhook import Webhook
from typing import Any, Callable, Iterable, Mapping, TypeVar, overload

__all__ = ['TextChannel', 'VoiceChannel', 'StageChannel', 'DMChannel', 'CategoryChannel', 'GroupChannel', 'PartialMessageable', 'ForumChannel', 'ForumTag']

class ForumTag(Hashable):
    name: str
    id: int
    moderated: bool
    emoji: PartialEmoji
    def __init__(self, *, name: str, emoji: EmojiInputType, moderated: bool = False) -> None: ...
    @classmethod
    def from_data(cls, *, state: ConnectionState, data: ForumTagPayload) -> ForumTag: ...
    def to_dict(self) -> dict[str, Any]: ...

class _TextChannel(discord.abc.GuildChannel, Hashable):
    id: int
    def __init__(self, *, state: ConnectionState, guild: Guild, data: TextChannelPayload | ForumChannelPayload) -> None: ...
    @property
    def type(self) -> ChannelType: ...
    def permissions_for(self, obj: Member | Role, /) -> Permissions: ...
    @property
    def members(self) -> list[Member]: ...
    @property
    def threads(self) -> list[Thread]: ...
    def is_nsfw(self) -> bool: ...
    @property
    def last_message(self) -> Message | None: ...
    async def edit(self, **options) -> _TextChannel: ...
    async def clone(self, *, name: str | None = None, reason: str | None = None) -> TextChannel: ...
    async def delete_messages(self, messages: Iterable[Snowflake], *, reason: str | None = None) -> None: ...
    async def purge(self, *, limit: int | None = 100, check: Callable[[Message], bool] = ..., before: SnowflakeTime | None = None, after: SnowflakeTime | None = None, around: SnowflakeTime | None = None, oldest_first: bool | None = False, bulk: bool = True, reason: str | None = None) -> list[Message]: ...
    async def webhooks(self) -> list[Webhook]: ...
    async def create_webhook(self, *, name: str, avatar: bytes | None = None, reason: str | None = None) -> Webhook: ...
    async def follow(self, *, destination: TextChannel, reason: str | None = None) -> Webhook: ...
    def get_partial_message(self, message_id: int, /) -> PartialMessage: ...
    def get_thread(self, thread_id: int, /) -> Thread | None: ...
    def archived_threads(self, *, private: bool = False, joined: bool = False, limit: int | None = 50, before: Snowflake | datetime.datetime | None = None) -> ArchivedThreadIterator: ...

class TextChannel(discord.abc.Messageable, _TextChannel):
    def __init__(self, *, state: ConnectionState, guild: Guild, data: TextChannelPayload) -> None: ...
    def is_news(self) -> bool: ...
    @property
    def news(self) -> bool: ...
    @overload
    async def edit(self, *, reason: str | None = ..., name: str = ..., topic: str = ..., position: int = ..., nsfw: bool = ..., sync_permissions: bool = ..., category: CategoryChannel | None = ..., slowmode_delay: int = ..., default_auto_archive_duration: ThreadArchiveDuration = ..., default_thread_slowmode_delay: int = ..., type: ChannelType = ..., overwrites: Mapping[Role | Member | Snowflake, PermissionOverwrite] = ...) -> TextChannel | None: ...
    @overload
    async def edit(self) -> TextChannel | None: ...
    async def create_thread(self, *, name: str, message: Snowflake | None = None, auto_archive_duration: ThreadArchiveDuration = ..., type: ChannelType | None = None, slowmode_delay: int | None = None, invitable: bool | None = None, reason: str | None = None) -> Thread: ...

class ForumChannel(_TextChannel):
    def __init__(self, *, state: ConnectionState, guild: Guild, data: ForumChannelPayload) -> None: ...
    @property
    def guidelines(self) -> str | None: ...
    @property
    def requires_tag(self) -> bool: ...
    def get_tag(self, id: int, /) -> ForumTag | None: ...
    @overload
    async def edit(self, *, reason: str | None = ..., name: str = ..., topic: str = ..., position: int = ..., nsfw: bool = ..., sync_permissions: bool = ..., category: CategoryChannel | None = ..., slowmode_delay: int = ..., default_auto_archive_duration: ThreadArchiveDuration = ..., default_thread_slowmode_delay: int = ..., default_sort_order: SortOrder = ..., default_reaction_emoji: Emoji | int | str | None = ..., available_tags: list[ForumTag] = ..., require_tag: bool = ..., overwrites: Mapping[Role | Member | Snowflake, PermissionOverwrite] = ...) -> ForumChannel | None: ...
    @overload
    async def edit(self) -> ForumChannel | None: ...
    async def create_thread(self, name: str, content=None, *, embed=None, embeds=None, file=None, files=None, stickers=None, delete_message_after=None, nonce=None, allowed_mentions=None, view=None, applied_tags=None, auto_archive_duration: ThreadArchiveDuration = ..., slowmode_delay: int = ..., reason: str | None = None) -> Thread: ...

class VocalGuildChannel(discord.abc.Connectable, discord.abc.GuildChannel, Hashable):
    id: int
    def __init__(self, *, state: ConnectionState, guild: Guild, data: VoiceChannelPayload | StageChannelPayload) -> None: ...
    @property
    def members(self) -> list[Member]: ...
    @property
    def voice_states(self) -> dict[int, VoiceState]: ...
    def permissions_for(self, obj: Member | Role, /) -> Permissions: ...

class VoiceChannel(discord.abc.Messageable, VocalGuildChannel):
    status: str | None
    def __init__(self, *, state: ConnectionState, guild: Guild, data: VoiceChannelPayload) -> None: ...
    def is_nsfw(self) -> bool: ...
    @property
    def last_message(self) -> Message | None: ...
    def get_partial_message(self, message_id: int, /) -> PartialMessage: ...
    async def delete_messages(self, messages: Iterable[Snowflake], *, reason: str | None = None) -> None: ...
    async def purge(self, *, limit: int | None = 100, check: Callable[[Message], bool] = ..., before: SnowflakeTime | None = None, after: SnowflakeTime | None = None, around: SnowflakeTime | None = None, oldest_first: bool | None = False, bulk: bool = True, reason: str | None = None) -> list[Message]: ...
    async def webhooks(self) -> list[Webhook]: ...
    async def create_webhook(self, *, name: str, avatar: bytes | None = None, reason: str | None = None) -> Webhook: ...
    @property
    def type(self) -> ChannelType: ...
    async def clone(self, *, name: str | None = None, reason: str | None = None) -> VoiceChannel: ...
    @overload
    async def edit(self, *, name: str = ..., bitrate: int = ..., user_limit: int = ..., position: int = ..., sync_permissions: int = ..., category: CategoryChannel | None = ..., overwrites: Mapping[Role | Member, PermissionOverwrite] = ..., rtc_region: VoiceRegion | None = ..., video_quality_mode: VideoQualityMode = ..., slowmode_delay: int = ..., reason: str | None = ...) -> VoiceChannel | None: ...
    @overload
    async def edit(self) -> VoiceChannel | None: ...
    async def create_activity_invite(self, activity: EmbeddedActivity | int, **kwargs) -> Invite: ...
    async def set_status(self, status: str | None, *, reason: str | None = None) -> None: ...

class StageChannel(discord.abc.Messageable, VocalGuildChannel):
    @property
    def requesting_to_speak(self) -> list[Member]: ...
    @property
    def speakers(self) -> list[Member]: ...
    @property
    def listeners(self) -> list[Member]: ...
    def is_nsfw(self) -> bool: ...
    @property
    def last_message(self) -> Message | None: ...
    def get_partial_message(self, message_id: int, /) -> PartialMessage: ...
    async def delete_messages(self, messages: Iterable[Snowflake], *, reason: str | None = None) -> None: ...
    async def purge(self, *, limit: int | None = 100, check: Callable[[Message], bool] = ..., before: SnowflakeTime | None = None, after: SnowflakeTime | None = None, around: SnowflakeTime | None = None, oldest_first: bool | None = False, bulk: bool = True, reason: str | None = None) -> list[Message]: ...
    async def webhooks(self) -> list[Webhook]: ...
    async def create_webhook(self, *, name: str, avatar: bytes | None = None, reason: str | None = None) -> Webhook: ...
    @property
    def moderators(self) -> list[Member]: ...
    @property
    def type(self) -> ChannelType: ...
    async def clone(self, *, name: str | None = None, reason: str | None = None) -> StageChannel: ...
    @property
    def instance(self) -> StageInstance | None: ...
    async def create_instance(self, *, topic: str, privacy_level: StagePrivacyLevel = ..., reason: str | None = None, send_notification: bool | None = False) -> StageInstance: ...
    async def fetch_instance(self) -> StageInstance: ...
    @overload
    async def edit(self, *, name: str = ..., topic: str | None = ..., position: int = ..., sync_permissions: int = ..., category: CategoryChannel | None = ..., overwrites: Mapping[Role | Member, PermissionOverwrite] = ..., rtc_region: VoiceRegion | None = ..., video_quality_mode: VideoQualityMode = ..., reason: str | None = ...) -> StageChannel | None: ...
    @overload
    async def edit(self) -> StageChannel | None: ...

class CategoryChannel(discord.abc.GuildChannel, Hashable):
    id: int
    def __init__(self, *, state: ConnectionState, guild: Guild, data: CategoryChannelPayload) -> None: ...
    @property
    def type(self) -> ChannelType: ...
    def is_nsfw(self) -> bool: ...
    async def clone(self, *, name: str | None = None, reason: str | None = None) -> CategoryChannel: ...
    @overload
    async def edit(self, *, name: str = ..., position: int = ..., nsfw: bool = ..., overwrites: Mapping[Role | Member, PermissionOverwrite] = ..., reason: str | None = ...) -> CategoryChannel | None: ...
    @overload
    async def edit(self) -> CategoryChannel | None: ...
    async def move(self, **kwargs) -> None: ...
    @property
    def channels(self) -> list[GuildChannelType]: ...
    @property
    def text_channels(self) -> list[TextChannel]: ...
    @property
    def voice_channels(self) -> list[VoiceChannel]: ...
    @property
    def stage_channels(self) -> list[StageChannel]: ...
    @property
    def forum_channels(self) -> list[ForumChannel]: ...
    async def create_text_channel(self, name: str, **options: Any) -> TextChannel: ...
    async def create_voice_channel(self, name: str, **options: Any) -> VoiceChannel: ...
    async def create_stage_channel(self, name: str, **options: Any) -> StageChannel: ...
    async def create_forum_channel(self, name: str, **options: Any) -> ForumChannel: ...
DMC = TypeVar('DMC', bound='DMChannel')

class DMChannel(discord.abc.Messageable, Hashable):
    recipient: User | None
    me: ClientUser
    id: int
    def __init__(self, *, me: ClientUser, state: ConnectionState, data: DMChannelPayload) -> None: ...
    @property
    def type(self) -> ChannelType: ...
    @property
    def jump_url(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    def permissions_for(self, obj: Any = None, /) -> Permissions: ...
    def get_partial_message(self, message_id: int, /) -> PartialMessage: ...

class GroupChannel(discord.abc.Messageable, Hashable):
    id: int
    me: ClientUser
    def __init__(self, *, me: ClientUser, state: ConnectionState, data: GroupChannelPayload) -> None: ...
    @property
    def type(self) -> ChannelType: ...
    @property
    def icon(self) -> Asset | None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def jump_url(self) -> str: ...
    def permissions_for(self, obj: Snowflake, /) -> Permissions: ...
    async def leave(self) -> None: ...

class PartialMessageable(discord.abc.Messageable, Hashable):
    id: int
    type: ChannelType | None
    def __init__(self, state: ConnectionState, id: int, type: ChannelType | None = None) -> None: ...
    def get_partial_message(self, message_id: int, /) -> PartialMessage: ...
