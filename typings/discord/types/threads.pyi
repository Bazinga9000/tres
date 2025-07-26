from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from ..flags import ChannelFlags as ChannelFlags
from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete

ThreadType: Incomplete
ThreadArchiveDuration: Incomplete

class ThreadMember(TypedDict):
    id: Snowflake
    user_id: Snowflake
    join_timestamp: str
    flags: int

class ThreadMetadata(TypedDict):
    invitable: NotRequired[bool]
    create_timestamp: NotRequired[str]
    archived: bool
    auto_archive_duration: ThreadArchiveDuration
    archive_timestamp: str
    locked: bool

class Thread(TypedDict):
    member: NotRequired[ThreadMember]
    last_message_id: NotRequired[Snowflake | None]
    last_pin_timestamp: NotRequired[Snowflake | None]
    id: Snowflake
    guild_id: Snowflake
    parent_id: Snowflake
    owner_id: Snowflake
    name: str
    type: ThreadType
    member_count: int
    message_count: int
    rate_limit_per_user: int
    thread_metadata: ThreadMetadata
    flags: ChannelFlags
    total_message_sent: int

class ThreadPaginationPayload(TypedDict):
    threads: list[Thread]
    members: list[ThreadMember]
    has_more: bool
