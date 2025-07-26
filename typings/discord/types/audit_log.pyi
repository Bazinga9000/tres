from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .automod import AutoModRule as AutoModRule
from .channel import ChannelType as ChannelType, PermissionOverwrite as PermissionOverwrite, VideoQualityMode as VideoQualityMode
from .guild import DefaultMessageNotificationLevel as DefaultMessageNotificationLevel, ExplicitContentFilterLevel as ExplicitContentFilterLevel, MFALevel as MFALevel, VerificationLevel as VerificationLevel
from .integration import IntegrationExpireBehavior as IntegrationExpireBehavior, PartialIntegration as PartialIntegration
from .role import Role as Role
from .scheduled_events import ScheduledEvent as ScheduledEvent
from .snowflake import Snowflake as Snowflake
from .threads import Thread as Thread
from .user import User as User
from .webhook import Webhook as Webhook
from _typeshed import Incomplete
from typing import Literal

AuditLogEvent: Incomplete

class _AuditLogChange_Str(TypedDict):
    key: Literal['name', 'description', 'preferred_locale', 'vanity_url_code', 'topic', 'code', 'allow', 'deny', 'permissions', 'tags', 'status']
    new_value: str
    old_value: str

class _AuditLogChange_AssetHash(TypedDict):
    key: Literal['icon_hash', 'splash_hash', 'discovery_splash_hash', 'banner_hash', 'avatar_hash', 'asset']
    new_value: str
    old_value: str

class _AuditLogChange_Snowflake(TypedDict):
    key: Literal['id', 'owner_id', 'afk_channel_id', 'rules_channel_id', 'public_updates_channel_id', 'widget_channel_id', 'system_channel_id', 'application_id', 'channel_id', 'inviter_id', 'guild_id']
    new_value: Snowflake
    old_value: Snowflake

class _AuditLogChange_Bool(TypedDict):
    key: Literal['widget_enabled', 'nsfw', 'hoist', 'mentionable', 'temporary', 'deaf', 'mute', 'nick', 'enabled_emoticons', 'rtc_region', 'available', 'archived', 'locked']
    new_value: bool
    old_value: bool

class _AuditLogChange_Int(TypedDict):
    key: Literal['afk_timeout', 'prune_delete_days', 'position', 'bitrate', 'rate_limit_per_user', 'color', 'max_uses', 'max_age', 'user_limit', 'auto_archive_duration', 'default_auto_archive_duration']
    new_value: int
    old_value: int

class _AuditLogChange_ListRole(TypedDict):
    key: Literal['$add', '$remove']
    new_value: list[Role]
    old_value: list[Role]

class _AuditLogChange_MFALevel(TypedDict):
    key: Literal['mfa_level']
    new_value: MFALevel
    old_value: MFALevel

class _AuditLogChange_VerificationLevel(TypedDict):
    key: Literal['verification_level']
    new_value: VerificationLevel
    old_value: VerificationLevel

class _AuditLogChange_ExplicitContentFilter(TypedDict):
    key: Literal['explicit_content_filter']
    new_value: ExplicitContentFilterLevel
    old_value: ExplicitContentFilterLevel

class _AuditLogChange_DefaultMessageNotificationLevel(TypedDict):
    key: Literal['default_message_notifications']
    new_value: DefaultMessageNotificationLevel
    old_value: DefaultMessageNotificationLevel

class _AuditLogChange_ChannelType(TypedDict):
    key: Literal['type']
    new_value: ChannelType
    old_value: ChannelType

class _AuditLogChange_IntegrationExpireBehaviour(TypedDict):
    key: Literal['expire_behavior']
    new_value: IntegrationExpireBehavior
    old_value: IntegrationExpireBehavior

class _AuditLogChange_VideoQualityMode(TypedDict):
    key: Literal['video_quality_mode']
    new_value: VideoQualityMode
    old_value: VideoQualityMode

class _AuditLogChange_Overwrites(TypedDict):
    key: Literal['permission_overwrites']
    new_value: list[PermissionOverwrite]
    old_value: list[PermissionOverwrite]

AuditLogChange: Incomplete

class AuditEntryInfo(TypedDict):
    delete_member_days: str
    members_removed: str
    channel_id: Snowflake
    message_id: Snowflake
    count: str
    id: Snowflake
    type: Literal['0', '1']
    role_name: str
    application_id: Snowflake
    auto_moderation_rule_name: str
    auto_moderation_rule_trigger_type: str
    status: str

class AuditLogEntry(TypedDict):
    changes: NotRequired[list[AuditLogChange]]
    options: NotRequired[AuditEntryInfo]
    reason: NotRequired[str]
    target_id: str | None
    user_id: Snowflake | None
    id: Snowflake
    action_type: AuditLogEvent

class AuditLog(TypedDict):
    webhooks: list[Webhook]
    users: list[User]
    audit_log_entries: list[AuditLogEntry]
    integrations: list[PartialIntegration]
    threads: list[Thread]
    scheduled_events: list[ScheduledEvent]
    auto_moderation_rules: list[AutoModRule]
