from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete

AutoModTriggerType: Incomplete
AutoModEventType: Incomplete
AutoModActionType: Incomplete
AutoModKeywordPresetType: Incomplete

class AutoModTriggerMetadata(TypedDict, total=False):
    keyword_filter: list[str]
    regex_patterns: list[str]
    presets: list[AutoModKeywordPresetType]
    allow_list: list[str]
    mention_total_limit: int

class AutoModActionMetadata(TypedDict, total=False):
    channel_id: Snowflake
    duration_seconds: int
    custom_message: str

class AutoModAction(TypedDict):
    type: AutoModActionType
    metadata: AutoModActionMetadata

class AutoModRule(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModEventType
    trigger_type: AutoModTriggerType
    trigger_metadata: AutoModTriggerMetadata
    actions: list[AutoModAction]
    enabled: bool
    exempt_roles: list[Snowflake]
    exempt_channels: list[Snowflake]

class CreateAutoModRule(TypedDict):
    enabled: NotRequired[bool]
    exempt_roles: NotRequired[list[Snowflake]]
    exempt_channels: NotRequired[list[Snowflake]]
    name: str
    event_type: AutoModEventType
    trigger_type: AutoModTriggerType
    trigger_metadata: AutoModTriggerMetadata
    actions: list[AutoModAction]

class EditAutoModRule(TypedDict, total=False):
    name: str
    event_type: AutoModEventType
    trigger_metadata: AutoModTriggerMetadata
    actions: list[AutoModAction]
    enabled: bool
    exempt_roles: list[Snowflake]
    exempt_channels: list[Snowflake]
