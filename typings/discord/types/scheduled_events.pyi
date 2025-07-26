from .member import Member as Member
from .snowflake import Snowflake as Snowflake
from .user import User as User
from _typeshed import Incomplete
from typing import TypedDict

ScheduledEventStatus: Incomplete
ScheduledEventLocationType: Incomplete
ScheduledEventPrivacyLevel: Incomplete

class ScheduledEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    creator_id: Snowflake
    name: str
    description: str
    image: str | None
    scheduled_start_time: str
    scheduled_end_time: str | None
    privacy_level: ScheduledEventPrivacyLevel
    status: ScheduledEventStatus
    entity_type: ScheduledEventLocationType
    entity_id: Snowflake
    entity_metadata: ScheduledEventEntityMetadata
    creator: User
    user_count: int | None

class ScheduledEventEntityMetadata(TypedDict):
    location: str

class ScheduledEventSubscriber(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    user: User
    member: Member | None
