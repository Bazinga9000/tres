from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from .team import Team as Team
from .user import User as User

class BaseAppInfo(TypedDict):
    id: Snowflake
    name: str
    verify_key: str
    icon: str | None
    summary: str
    description: str
    terms_of_service_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    hook: NotRequired[bool]
    max_participants: NotRequired[int]

class AppInfo(BaseAppInfo):
    team: NotRequired[Team]
    guild_id: NotRequired[Snowflake]
    primary_sku_id: NotRequired[Snowflake]
    slug: NotRequired[str]
    rpc_origins: list[str]
    owner: User
    bot_public: bool
    bot_require_code_grant: bool

class PartialAppInfo(BaseAppInfo):
    rpc_origins: NotRequired[list[str]]
    cover_image: NotRequired[str]
    flags: NotRequired[int]
