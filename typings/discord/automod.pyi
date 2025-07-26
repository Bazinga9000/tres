from .abc import Snowflake
from .channel import ForumChannel, TextChannel, VoiceChannel
from .enums import AutoModActionType, AutoModEventType, AutoModKeywordPresetType, AutoModTriggerType
from .guild import Guild
from .member import Member
from .mixins import Hashable
from .object import Object
from .role import Role
from .state import ConnectionState
from .types.automod import AutoModAction as AutoModActionPayload, AutoModActionMetadata as AutoModActionMetadataPayload, AutoModRule as AutoModRulePayload, AutoModTriggerMetadata as AutoModTriggerMetadataPayload
from _typeshed import Incomplete
from datetime import timedelta
from functools import cached_property

__all__ = ['AutoModRule', 'AutoModAction', 'AutoModActionMetadata', 'AutoModTriggerMetadata']

class AutoModActionMetadata:
    channel_id: int
    timeout_duration: timedelta
    custom_message: str
    def __init__(self, channel_id: int = ..., timeout_duration: timedelta = ..., custom_message: str = ...) -> None: ...
    def to_dict(self) -> dict: ...
    @classmethod
    def from_dict(cls, data: AutoModActionMetadataPayload): ...

class AutoModAction:
    type: AutoModActionType
    metadata: AutoModActionMetadata
    def __init__(self, action_type: AutoModActionType, metadata: AutoModActionMetadata) -> None: ...
    def to_dict(self) -> dict: ...
    @classmethod
    def from_dict(cls, data: AutoModActionPayload): ...

class AutoModTriggerMetadata:
    keyword_filter: Incomplete
    regex_patterns: Incomplete
    presets: Incomplete
    allow_list: Incomplete
    mention_total_limit: Incomplete
    def __init__(self, keyword_filter: list[str] = ..., regex_patterns: list[str] = ..., presets: list[AutoModKeywordPresetType] = ..., allow_list: list[str] = ..., mention_total_limit: int = ...) -> None: ...
    def to_dict(self) -> dict: ...
    @classmethod
    def from_dict(cls, data: AutoModTriggerMetadataPayload): ...

class AutoModRule(Hashable):
    id: int
    guild_id: int
    name: str
    creator_id: int
    event_type: AutoModEventType
    trigger_type: AutoModTriggerType
    trigger_metadata: AutoModTriggerMetadata
    actions: list[AutoModAction]
    enabled: bool
    exempt_role_ids: list[int]
    exempt_channel_ids: list[int]
    def __init__(self, *, state: ConnectionState, data: AutoModRulePayload) -> None: ...
    @cached_property
    def guild(self) -> Guild | None: ...
    @cached_property
    def creator(self) -> Member | None: ...
    @cached_property
    def exempt_roles(self) -> list[Role | Object]: ...
    @cached_property
    def exempt_channels(self) -> list[TextChannel | ForumChannel | VoiceChannel | Object]: ...
    async def delete(self, reason: str | None = None) -> None: ...
    async def edit(self, *, name: str = ..., event_type: AutoModEventType = ..., trigger_metadata: AutoModTriggerMetadata = ..., actions: list[AutoModAction] = ..., enabled: bool = ..., exempt_roles: list[Snowflake] = ..., exempt_channels: list[Snowflake] = ..., reason: str | None = None) -> AutoModRule | None: ...
