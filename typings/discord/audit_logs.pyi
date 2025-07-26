import datetime
from . import abc, enums, utils
from .emoji import Emoji
from .guild import Guild
from .invite import Invite
from .member import Member
from .mixins import Hashable
from .object import Object
from .role import Role
from .stage_instance import StageInstance
from .state import ConnectionState
from .sticker import GuildSticker
from .threads import Thread
from .types.audit_log import AuditLogChange as AuditLogChangePayload, AuditLogEntry as AuditLogEntryPayload
from .user import User
from _typeshed import Incomplete
from typing import Any, ClassVar, Generator, TypeVar

__all__ = ['AuditLogDiff', 'AuditLogChanges', 'AuditLogEntry']

T = TypeVar('T', bound=enums.Enum)

class AuditLogDiff:
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[tuple[str, Any], None, None]: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> Any: ...

class AuditLogChanges:
    TRANSFORMERS: ClassVar[dict[str, tuple[str | None, Transformer | None]]]
    before: Incomplete
    after: Incomplete
    def __init__(self, entry: AuditLogEntry, data: list[AuditLogChangePayload], *, state: ConnectionState) -> None: ...

class _AuditLogProxyMemberPrune:
    delete_member_days: int
    members_removed: int

class _AuditLogProxyMemberMoveOrMessageDelete:
    channel: abc.GuildChannel
    count: int

class _AuditLogProxyMemberDisconnect:
    count: int

class _AuditLogProxyPinAction:
    channel: abc.GuildChannel
    message_id: int

class _AuditLogProxyStageInstanceAction:
    channel: abc.GuildChannel

class AuditLogEntry(Hashable):
    guild: Incomplete
    def __init__(self, *, users: dict[int, User], data: AuditLogEntryPayload, guild: Guild) -> None: ...
    @utils.cached_property
    def created_at(self) -> datetime.datetime: ...
    @utils.cached_property
    def target(self) -> Guild | abc.GuildChannel | Member | User | Role | Invite | Emoji | StageInstance | GuildSticker | Thread | Object | None: ...
    @utils.cached_property
    def category(self) -> enums.AuditLogActionCategory: ...
    @utils.cached_property
    def changes(self) -> AuditLogChanges: ...
    @utils.cached_property
    def before(self) -> AuditLogDiff: ...
    @utils.cached_property
    def after(self) -> AuditLogDiff: ...
