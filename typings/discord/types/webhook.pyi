from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .channel import PartialChannel as PartialChannel
from .snowflake import Snowflake as Snowflake
from .user import User as User
from _typeshed import Incomplete

class SourceGuild(TypedDict):
    id: int
    name: str
    icon: str

WebhookType: Incomplete

class PartialWebhook(TypedDict):
    guild_id: NotRequired[Snowflake]
    user: NotRequired[User]
    token: NotRequired[str]
    id: Snowflake
    type: WebhookType

class FollowerWebhook(PartialWebhook):
    source_channel: NotRequired[PartialChannel]
    source_guild: NotRequired[SourceGuild]
    channel_id: Snowflake
    webhook_id: Snowflake

class Webhook(PartialWebhook):
    name: NotRequired[str | None]
    avatar: NotRequired[str | None]
    channel_id: NotRequired[Snowflake]
    application_id: NotRequired[Snowflake | None]
