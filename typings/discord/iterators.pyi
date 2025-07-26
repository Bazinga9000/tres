import asyncio
import datetime
from .abc import Snowflake
from .audit_logs import AuditLogEntry
from .guild import BanEntry, Guild
from .member import Member
from .message import Message
from .monetization import Entitlement
from .object import Object
from .scheduled_events import ScheduledEvent
from .threads import Thread
from .types.threads import Thread as ThreadPayload
from .user import User
from _typeshed import Incomplete
from typing import Any, AsyncIterator, Awaitable, Callable, TypeVar

__all__ = ['ReactionIterator', 'HistoryIterator', 'AuditLogIterator', 'GuildIterator', 'MemberIterator', 'ScheduledEventSubscribersIterator', 'EntitlementIterator']

T = TypeVar('T')
OT = TypeVar('OT')

class _AsyncIterator(AsyncIterator[T]):
    async def next(self) -> T: ...
    def get(self, **attrs: Any) -> Awaitable[T | None]: ...
    async def find(self, predicate: _Func[T, bool]) -> T | None: ...
    def chunk(self, max_size: int) -> _ChunkedAsyncIterator[T]: ...
    def map(self, func: _Func[T, OT]) -> _MappedAsyncIterator[OT]: ...
    def filter(self, predicate: _Func[T, bool]) -> _FilteredAsyncIterator[T]: ...
    async def flatten(self) -> list[T]: ...
    async def __anext__(self) -> T: ...

class _ChunkedAsyncIterator(_AsyncIterator[list[T]]):
    iterator: Incomplete
    max_size: Incomplete
    def __init__(self, iterator, max_size) -> None: ...
    async def next(self) -> list[T]: ...

class _MappedAsyncIterator(_AsyncIterator[T]):
    iterator: Incomplete
    func: Incomplete
    def __init__(self, iterator, func) -> None: ...
    async def next(self) -> T: ...

class _FilteredAsyncIterator(_AsyncIterator[T]):
    iterator: Incomplete
    predicate: Incomplete
    def __init__(self, iterator, predicate) -> None: ...
    async def next(self) -> T: ...

class ReactionIterator(_AsyncIterator['User' | 'Member']):
    message: Incomplete
    limit: Incomplete
    after: Incomplete
    type: Incomplete
    getter: Incomplete
    state: Incomplete
    emoji: Incomplete
    guild: Incomplete
    channel_id: Incomplete
    users: Incomplete
    def __init__(self, message, emoji, limit: int = 100, after=None, type=None) -> None: ...
    async def next(self) -> User | Member: ...
    async def fill_users(self) -> None: ...

class VoteIterator(_AsyncIterator['User' | 'Member']):
    message: Incomplete
    limit: Incomplete
    after: Incomplete
    getter: Incomplete
    state: Incomplete
    answer: Incomplete
    guild: Incomplete
    channel_id: Incomplete
    users: Incomplete
    def __init__(self, message, answer, limit: int = 100, after=None) -> None: ...
    async def next(self) -> User | Member: ...
    async def fill_users(self) -> None: ...

class HistoryIterator(_AsyncIterator['Message']):
    reverse: Incomplete
    messageable: Incomplete
    limit: Incomplete
    before: Incomplete
    after: Incomplete
    around: Incomplete
    state: Incomplete
    logs_from: Incomplete
    messages: Incomplete
    def __init__(self, messageable, limit, before=None, after=None, around=None, oldest_first=None) -> None: ...
    async def next(self) -> Message: ...
    channel: Incomplete
    async def fill_messages(self) -> None: ...

class AuditLogIterator(_AsyncIterator['AuditLogEntry']):
    guild: Incomplete
    loop: Incomplete
    request: Incomplete
    limit: Incomplete
    before: Incomplete
    user_id: Incomplete
    action_type: Incomplete
    after: Incomplete
    entries: Incomplete
    def __init__(self, guild, limit=None, before=None, after=None, user_id=None, action_type=None) -> None: ...
    async def next(self) -> AuditLogEntry: ...

class GuildIterator(_AsyncIterator['Guild']):
    bot: Incomplete
    limit: Incomplete
    before: Incomplete
    after: Incomplete
    state: Incomplete
    get_guilds: Incomplete
    guilds: Incomplete
    def __init__(self, bot, limit, before=None, after=None) -> None: ...
    async def next(self) -> Guild: ...
    def create_guild(self, data): ...
    async def fill_guilds(self) -> None: ...

class MemberIterator(_AsyncIterator['Member']):
    guild: Incomplete
    limit: Incomplete
    after: Incomplete
    state: Incomplete
    get_members: Incomplete
    members: Incomplete
    def __init__(self, guild, limit: int = 1000, after=None) -> None: ...
    async def next(self) -> Member: ...
    async def fill_members(self) -> None: ...
    def create_member(self, data): ...

class BanIterator(_AsyncIterator['BanEntry']):
    guild: Incomplete
    limit: Incomplete
    after: Incomplete
    before: Incomplete
    state: Incomplete
    get_bans: Incomplete
    bans: Incomplete
    def __init__(self, guild, limit=None, before=None, after=None) -> None: ...
    async def next(self) -> BanEntry: ...
    async def fill_bans(self) -> None: ...
    def create_ban(self, data): ...

class ArchivedThreadIterator(_AsyncIterator['Thread']):
    channel_id: Incomplete
    guild: Incomplete
    limit: Incomplete
    joined: Incomplete
    private: Incomplete
    http: Incomplete
    before: str | None
    update_before: Callable[[ThreadPayload], str]
    endpoint: Incomplete
    queue: asyncio.Queue[Thread]
    has_more: bool
    def __init__(self, channel_id: int, guild: Guild, limit: int | None, joined: bool, private: bool, before: Snowflake | datetime.datetime | None = None) -> None: ...
    async def next(self) -> Thread: ...
    @staticmethod
    def get_archive_timestamp(data: ThreadPayload) -> str: ...
    @staticmethod
    def get_thread_id(data: ThreadPayload) -> str: ...
    async def fill_queue(self) -> None: ...
    def create_thread(self, data: ThreadPayload) -> Thread: ...

class ScheduledEventSubscribersIterator(_AsyncIterator['User' | 'Member']):
    event: Incomplete
    limit: Incomplete
    with_member: Incomplete
    before: Incomplete
    after: Incomplete
    subscribers: Incomplete
    get_subscribers: Incomplete
    def __init__(self, event: ScheduledEvent, limit: int | None, with_member: bool = False, before: datetime.datetime | int | None = None, after: datetime.datetime | int | None = None) -> None: ...
    async def next(self) -> User | Member: ...
    def member_from_payload(self, data): ...
    def user_from_payload(self, data): ...
    async def fill_subs(self) -> None: ...

class EntitlementIterator(_AsyncIterator['Entitlement']):
    user_id: Incomplete
    sku_ids: Incomplete
    before: Incomplete
    after: Incomplete
    limit: Incomplete
    guild_id: Incomplete
    exclude_ended: Incomplete
    state: Incomplete
    get_entitlements: Incomplete
    entitlements: Incomplete
    def __init__(self, state, user_id: int | None = None, sku_ids: list[int] | None = None, before: datetime.datetime | Object | None = None, after: datetime.datetime | Object | None = None, limit: int | None = None, guild_id: int | None = None, exclude_ended: bool | None = None) -> None: ...
    async def next(self) -> Entitlement: ...
    async def fill_entitlements(self) -> None: ...
