from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from .user import User as User
from _typeshed import Incomplete

class IntegrationApplication(TypedDict):
    bot: NotRequired[User]
    id: Snowflake
    name: str
    icon: str | None
    description: str
    summary: str

class IntegrationAccount(TypedDict):
    id: str
    name: str

IntegrationExpireBehavior: Incomplete

class PartialIntegration(TypedDict):
    id: Snowflake
    name: str
    type: IntegrationType
    account: IntegrationAccount

IntegrationType: Incomplete

class BaseIntegration(PartialIntegration):
    enabled: bool
    syncing: bool
    synced_at: str
    user: User
    expire_behavior: IntegrationExpireBehavior
    expire_grace_period: int

class StreamIntegration(BaseIntegration):
    role_id: Snowflake | None
    enable_emoticons: bool
    subscriber_count: int
    revoked: bool

class BotIntegration(BaseIntegration):
    application: IntegrationApplication
Integration = BaseIntegration | StreamIntegration | BotIntegration
