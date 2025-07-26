from .asset import Asset
from .channel import CategoryChannel, DMChannel, GroupChannel, PartialMessageable, StageChannel, TextChannel, VoiceChannel
from .client import Client
from .context_managers import Typing
from .embeds import Embed
from .enums import ChannelType, InviteTarget
from .file import File
from .flags import ChannelFlags
from .guild import Guild
from .invite import Invite
from .iterators import HistoryIterator
from .member import Member
from .mentions import AllowedMentions
from .message import Message, MessageReference, PartialMessage
from .permissions import PermissionOverwrite, Permissions
from .poll import Poll
from .role import Role
from .scheduled_events import ScheduledEvent
from .state import ConnectionState
from .sticker import GuildSticker, StickerItem
from .threads import Thread
from .types.channel import OverwriteType, PermissionOverwrite as PermissionOverwritePayload
from .ui.view import View
from .user import ClientUser
from .voice_client import VoiceProtocol
from datetime import datetime
from typing import Any, Callable, Protocol, Sequence, TypeVar, overload

__all__ = ['Snowflake', 'User', 'PrivateChannel', 'GuildChannel', 'Messageable', 'Connectable', 'Mentionable']

T = TypeVar('T', bound=VoiceProtocol)
PartialMessageableChannel = TextChannel | VoiceChannel | StageChannel | Thread | DMChannel | PartialMessageable
MessageableChannel = PartialMessageableChannel | GroupChannel

class Snowflake(Protocol):
    id: int

class User(Snowflake, Protocol):
    name: str
    discriminator: str
    global_name: str | None
    avatar: Asset
    bot: bool
    @property
    def display_name(self) -> str: ...
    @property
    def mention(self) -> str: ...

class PrivateChannel(Snowflake, Protocol):
    me: ClientUser

class _Overwrites:
    ROLE: int
    MEMBER: int
    id: int
    allow: int
    deny: int
    type: OverwriteType
    def __init__(self, data: PermissionOverwritePayload) -> None: ...
    def is_role(self) -> bool: ...
    def is_member(self) -> bool: ...
GCH = TypeVar('GCH', bound='GuildChannel')

class GuildChannel:
    id: int
    name: str
    guild: Guild
    type: ChannelType
    position: int
    category_id: int | None
    flags: ChannelFlags
    def __init__(self, *, state: ConnectionState, guild: Guild, data: dict[str, Any]) -> None: ...
    @property
    def changed_roles(self) -> list[Role]: ...
    @property
    def mention(self) -> str: ...
    @property
    def jump_url(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    def overwrites_for(self, obj: Role | User) -> PermissionOverwrite: ...
    @property
    def overwrites(self) -> dict[Role | Member, PermissionOverwrite]: ...
    @property
    def category(self) -> CategoryChannel | None: ...
    @property
    def permissions_synced(self) -> bool: ...
    def permissions_for(self, obj: Member | Role, /) -> Permissions: ...
    async def delete(self, *, reason: str | None = None) -> None: ...
    @overload
    async def set_permissions(self, target: Member | Role, *, overwrite: PermissionOverwrite | None = ..., reason: str | None = ...) -> None: ...
    @overload
    async def set_permissions(self, target: Member | Role, *, reason: str | None = ..., **permissions: bool) -> None: ...
    async def clone(self, *, name: str | None = None, reason: str | None = None) -> GCH: ...
    @overload
    async def move(self, *, beginning: bool, offset: int = ..., category: Snowflake | None = ..., sync_permissions: bool = ..., reason: str | None = ...) -> None: ...
    @overload
    async def move(self, *, end: bool, offset: int = ..., category: Snowflake | None = ..., sync_permissions: bool = ..., reason: str = ...) -> None: ...
    @overload
    async def move(self, *, before: Snowflake, offset: int = ..., category: Snowflake | None = ..., sync_permissions: bool = ..., reason: str = ...) -> None: ...
    @overload
    async def move(self, *, after: Snowflake, offset: int = ..., category: Snowflake | None = ..., sync_permissions: bool = ..., reason: str = ...) -> None: ...
    async def create_invite(self, *, reason: str | None = None, max_age: int = 0, max_uses: int = 0, temporary: bool = False, unique: bool = True, target_event: ScheduledEvent | None = None, target_type: InviteTarget | None = None, target_user: User | None = None, target_application_id: int | None = None) -> Invite: ...
    async def invites(self) -> list[Invite]: ...

class Messageable:
    @overload
    async def send(self, content: str | None = ..., *, tts: bool = ..., embed: Embed = ..., file: File = ..., stickers: Sequence[GuildSticker | StickerItem] = ..., delete_after: float = ..., nonce: int | str = ..., enforce_nonce: bool = ..., allowed_mentions: AllowedMentions = ..., reference: Message | MessageReference | PartialMessage = ..., mention_author: bool = ..., view: View = ..., poll: Poll = ..., suppress: bool = ..., silent: bool = ...) -> Message: ...
    @overload
    async def send(self, content: str | None = ..., *, tts: bool = ..., embed: Embed = ..., files: list[File] = ..., stickers: Sequence[GuildSticker | StickerItem] = ..., delete_after: float = ..., nonce: int | str = ..., enforce_nonce: bool = ..., allowed_mentions: AllowedMentions = ..., reference: Message | MessageReference | PartialMessage = ..., mention_author: bool = ..., view: View = ..., poll: Poll = ..., suppress: bool = ..., silent: bool = ...) -> Message: ...
    @overload
    async def send(self, content: str | None = ..., *, tts: bool = ..., embeds: list[Embed] = ..., file: File = ..., stickers: Sequence[GuildSticker | StickerItem] = ..., delete_after: float = ..., nonce: int | str = ..., enforce_nonce: bool = ..., allowed_mentions: AllowedMentions = ..., reference: Message | MessageReference | PartialMessage = ..., mention_author: bool = ..., view: View = ..., poll: Poll = ..., suppress: bool = ..., silent: bool = ...) -> Message: ...
    @overload
    async def send(self, content: str | None = ..., *, tts: bool = ..., embeds: list[Embed] = ..., files: list[File] = ..., stickers: Sequence[GuildSticker | StickerItem] = ..., delete_after: float = ..., nonce: int | str = ..., enforce_nonce: bool = ..., allowed_mentions: AllowedMentions = ..., reference: Message | MessageReference | PartialMessage = ..., mention_author: bool = ..., view: View = ..., poll: Poll = ..., suppress: bool = ..., silent: bool = ...) -> Message: ...
    async def trigger_typing(self) -> None: ...
    def typing(self) -> Typing: ...
    async def fetch_message(self, id: int, /) -> Message: ...
    async def pins(self) -> list[Message]: ...
    def can_send(self, *objects) -> bool: ...
    def history(self, *, limit: int | None = 100, before: SnowflakeTime | None = None, after: SnowflakeTime | None = None, around: SnowflakeTime | None = None, oldest_first: bool | None = None) -> HistoryIterator: ...

class Connectable(Protocol):
    async def connect(self, *, timeout: float = 60.0, reconnect: bool = True, cls: Callable[[Client, Connectable], T] = ...) -> T: ...

class Mentionable: ...
