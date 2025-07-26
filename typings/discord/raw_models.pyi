import datetime
from .abc import MessageableChannel
from .automod import AutoModAction, AutoModTriggerType
from .enums import ChannelType, ReactionType
from .guild import Guild
from .member import Member
from .message import Message
from .partial_emoji import PartialEmoji
from .state import ConnectionState
from .threads import Thread
from .types.raw_models import AuditLogEntryEvent, AutoModActionExecutionEvent as AutoModActionExecution, BulkMessageDeleteEvent, IntegrationDeleteEvent, MemberRemoveEvent, MessageDeleteEvent, MessagePollVoteEvent, MessageUpdateEvent, ReactionActionEvent, ReactionClearEmojiEvent, ReactionClearEvent, ScheduledEventSubscription, ThreadDeleteEvent, ThreadMembersUpdateEvent, ThreadUpdateEvent, TypingEvent, VoiceChannelStatusUpdateEvent
from .user import User
from _typeshed import Incomplete

__all__ = ['RawMessageDeleteEvent', 'RawBulkMessageDeleteEvent', 'RawMessageUpdateEvent', 'RawReactionActionEvent', 'RawReactionClearEvent', 'RawReactionClearEmojiEvent', 'RawIntegrationDeleteEvent', 'RawThreadUpdateEvent', 'RawThreadDeleteEvent', 'RawTypingEvent', 'RawMemberRemoveEvent', 'RawScheduledEventSubscription', 'AutoModActionExecutionEvent', 'RawThreadMembersUpdateEvent', 'RawAuditLogEntryEvent', 'RawVoiceChannelStatusUpdateEvent', 'RawMessagePollVoteEvent']

class _RawReprMixin: ...

class RawMessageDeleteEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    cached_message: Message | None
    guild_id: int | None
    data: MessageDeleteEvent
    def __init__(self, data: MessageDeleteEvent) -> None: ...

class RawBulkMessageDeleteEvent(_RawReprMixin):
    message_ids: set[int]
    channel_id: int
    cached_messages: list[Message]
    guild_id: int | None
    data: BulkMessageDeleteEvent
    def __init__(self, data: BulkMessageDeleteEvent) -> None: ...

class RawMessageUpdateEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    data: MessageUpdateEvent
    cached_message: Message | None
    guild_id: int | None
    def __init__(self, data: MessageUpdateEvent) -> None: ...

class RawReactionActionEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    user_id: int
    emoji: PartialEmoji
    event_type: str
    member: Member | None
    burst: bool
    burst_colours: list
    burst_colors: list
    type: ReactionType
    guild_id: int | None
    data: ReactionActionEvent
    def __init__(self, data: ReactionActionEvent, emoji: PartialEmoji, event_type: str) -> None: ...

class RawReactionClearEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    guild_id: int | None
    data: ReactionClearEvent
    def __init__(self, data: ReactionClearEvent) -> None: ...

class RawReactionClearEmojiEvent(_RawReprMixin):
    emoji: PartialEmoji
    message_id: int
    channel_id: int
    burst: bool
    burst_colours: list
    burst_colors: list
    type: ReactionType
    guild_id: int | None
    data: ReactionClearEmojiEvent
    def __init__(self, data: ReactionClearEmojiEvent, emoji: PartialEmoji) -> None: ...

class RawIntegrationDeleteEvent(_RawReprMixin):
    integration_id: int
    guild_id: int
    application_id: int | None
    data: IntegrationDeleteEvent
    def __init__(self, data: IntegrationDeleteEvent) -> None: ...

class RawThreadUpdateEvent(_RawReprMixin):
    thread_id: int
    thread_type: ChannelType
    guild_id: int
    parent_id: int
    data: ThreadUpdateEvent
    thread: Thread | None
    def __init__(self, data: ThreadUpdateEvent) -> None: ...

class RawThreadDeleteEvent(_RawReprMixin):
    thread_id: int
    thread_type: ChannelType
    guild_id: int
    parent_id: int
    thread: Thread | None
    data: ThreadDeleteEvent
    def __init__(self, data: ThreadDeleteEvent) -> None: ...

class RawVoiceChannelStatusUpdateEvent(_RawReprMixin):
    id: int
    guild_id: int
    status: str | None
    data: VoiceChannelStatusUpdateEvent
    def __init__(self, data: VoiceChannelStatusUpdateEvent) -> None: ...

class RawTypingEvent(_RawReprMixin):
    channel_id: int
    user_id: int
    when: datetime.datetime
    member: Member | None
    guild_id: int | None
    data: TypingEvent
    def __init__(self, data: TypingEvent) -> None: ...

class RawMemberRemoveEvent(_RawReprMixin):
    user: User
    guild_id: int
    data: MemberRemoveEvent
    def __init__(self, data: MemberRemoveEvent, user: User) -> None: ...

class RawScheduledEventSubscription(_RawReprMixin):
    event_id: int
    user_id: int
    guild: Guild | None
    event_type: str
    data: ScheduledEventSubscription
    def __init__(self, data: ScheduledEventSubscription, event_type: str) -> None: ...

class AutoModActionExecutionEvent:
    action: AutoModAction
    rule_id: int
    rule_trigger_type: AutoModTriggerType
    guild_id: int
    guild: Guild | None
    user_id: int
    content: str | None
    matched_keyword: str
    matched_content: str | None
    member: Member | None
    channel_id: int | None
    channel: MessageableChannel | None
    message_id: int | None
    message: Message | None
    alert_system_message_id: int | None
    alert_system_message: Message | None
    data: AutoModActionExecution
    def __init__(self, state: ConnectionState, data: AutoModActionExecution) -> None: ...

class RawThreadMembersUpdateEvent(_RawReprMixin):
    thread_id: Incomplete
    guild_id: Incomplete
    member_count: Incomplete
    data: ThreadMembersUpdateEvent
    def __init__(self, data: ThreadMembersUpdateEvent) -> None: ...

class RawAuditLogEntryEvent(_RawReprMixin):
    id: Incomplete
    user_id: Incomplete
    guild_id: Incomplete
    target_id: Incomplete
    action_type: Incomplete
    reason: Incomplete
    extra: Incomplete
    changes: Incomplete
    data: AuditLogEntryEvent
    def __init__(self, data: AuditLogEntryEvent) -> None: ...

class RawMessagePollVoteEvent(_RawReprMixin):
    user_id: int
    channel_id: int
    message_id: int
    answer_id: int
    data: MessagePollVoteEvent
    added: bool
    guild_id: int | None
    def __init__(self, data: MessagePollVoteEvent, added: bool) -> None: ...
