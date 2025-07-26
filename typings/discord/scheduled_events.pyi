import datetime
from .abc import Snowflake
from .asset import Asset
from .enums import ScheduledEventLocationType, ScheduledEventPrivacyLevel, ScheduledEventStatus
from .guild import Guild
from .iterators import ScheduledEventSubscribersIterator
from .member import Member
from .mixins import Hashable
from .object import Object
from .state import ConnectionState
from .types.channel import StageChannel, VoiceChannel
from .types.scheduled_events import ScheduledEvent as ScheduledEventPayload
from _typeshed import Incomplete

__all__ = ['ScheduledEvent', 'ScheduledEventLocation']

class ScheduledEventLocation:
    value: str | StageChannel | VoiceChannel | Object
    def __init__(self, *, state: ConnectionState, value: str | int | StageChannel | VoiceChannel) -> None: ...
    @property
    def type(self) -> ScheduledEventLocationType: ...

class ScheduledEvent(Hashable):
    id: int
    guild: Guild
    name: str
    description: str | None
    start_time: datetime.datetime
    end_time: datetime.datetime | None
    status: ScheduledEventStatus
    subscriber_count: int | None
    creator_id: int | None
    creator: Member | None
    location: Incomplete
    def __init__(self, *, state: ConnectionState, guild: Guild, creator: Member | None, data: ScheduledEventPayload) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def interested(self) -> int | None: ...
    @property
    def url(self) -> str: ...
    @property
    def cover(self) -> Asset | None: ...
    async def edit(self, *, reason: str | None = None, name: str = ..., description: str = ..., status: int | ScheduledEventStatus = ..., location: str | int | VoiceChannel | StageChannel | ScheduledEventLocation = ..., start_time: datetime.datetime = ..., end_time: datetime.datetime = ..., cover: bytes | None = ..., privacy_level: ScheduledEventPrivacyLevel = ...) -> ScheduledEvent | None: ...
    async def delete(self) -> None: ...
    async def start(self, *, reason: str | None = None) -> None: ...
    async def complete(self, *, reason: str | None = None) -> None: ...
    async def cancel(self, *, reason: str | None = None) -> None: ...
    def subscribers(self, *, limit: int | None = 100, as_member: bool = False, before: Snowflake | datetime.datetime | None = None, after: Snowflake | datetime.datetime | None = None) -> ScheduledEventSubscribersIterator: ...
