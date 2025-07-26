from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .automod import AutoModAction as AutoModAction, AutoModTriggerType as AutoModTriggerType
from .emoji import PartialEmoji as PartialEmoji
from .member import Member as Member
from .snowflake import Snowflake as Snowflake
from .threads import Thread as Thread, ThreadMember as ThreadMember
from .user import User as User

class _MessageEventOptional(TypedDict, total=False):
    guild_id: Snowflake

class MessageDeleteEvent(_MessageEventOptional):
    id: Snowflake
    channel_id: Snowflake

class BulkMessageDeleteEvent(_MessageEventOptional):
    ids: list[Snowflake]
    channel_id: Snowflake

class MessageUpdateEvent(_MessageEventOptional):
    id: Snowflake
    channel_id: Snowflake

class _ReactionEventOptional(TypedDict, total=False):
    guild_id: Snowflake

class ReactionActionEvent(_ReactionEventOptional):
    member: NotRequired[Member]
    user_id: Snowflake
    channel_id: Snowflake
    message_id: Snowflake
    emoji: PartialEmoji
    burst: bool
    burst_colors: list
    type: int

class ReactionClearEvent(_ReactionEventOptional):
    channel_id: Snowflake
    message_id: Snowflake

class ReactionClearEmojiEvent(_ReactionEventOptional):
    channel_id: int
    message_id: int
    emoji: PartialEmoji
    burst: bool
    burst_colors: list
    type: int

class IntegrationDeleteEvent(TypedDict):
    application_id: NotRequired[Snowflake]
    id: Snowflake
    guild_id: Snowflake
ThreadUpdateEvent = Thread

class ThreadDeleteEvent(TypedDict, total=False):
    thread_id: Snowflake
    thread_type: int
    guild_id: Snowflake
    parent_id: Snowflake

class TypingEvent(TypedDict):
    guild_id: NotRequired[Snowflake]
    member: NotRequired[Member]
    channel_id: Snowflake
    user_id: Snowflake
    timestamp: int

class ScheduledEventSubscription(TypedDict, total=False):
    event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake

class AutoModActionExecutionEvent(TypedDict):
    channel_id: NotRequired[Snowflake]
    message_id: NotRequired[Snowflake]
    alert_system_message_id: NotRequired[Snowflake]
    matched_keyword: NotRequired[str]
    matched_content: NotRequired[str]
    guild_id: Snowflake
    action: AutoModAction
    rule_id: Snowflake
    rule_trigger_type: AutoModTriggerType
    user_id: Snowflake
    content: str

class MemberRemoveEvent(TypedDict):
    guild_id: Snowflake
    user: User

class VoiceChannelStatusUpdateEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    status: NotRequired[str]

class ThreadMembersUpdateEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    member_count: int
    added_members: NotRequired[list[ThreadMember]]
    removed_member_ids: NotRequired[list[Snowflake]]

class AuditLogEntryEvent(TypedDict):
    id: Snowflake
    user_id: NotRequired[Snowflake]
    guild_id: Snowflake
    target_id: NotRequired[Snowflake]
    action_type: int
    changes: NotRequired[list[dict]]
    reason: NotRequired[str]
    options: NotRequired[dict]

class MessagePollVoteEvent(TypedDict):
    user_id: Snowflake
    guild_id: NotRequired[Snowflake]
    channel_id: Snowflake
    message_id: Snowflake
    answer_id: int
