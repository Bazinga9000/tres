from .asset import Asset
from .guild import Guild
from .state import ConnectionState
from .types.appinfo import AppInfo as AppInfoPayload, PartialAppInfo as PartialAppInfoPayload
from .user import User

__all__ = ['AppInfo', 'PartialAppInfo']

class AppInfo:
    id: int
    name: str
    description: str
    rpc_origins: list[str]
    bot_public: bool
    bot_require_code_grant: bool
    owner: User
    team: Team | None
    summary: str
    verify_key: str
    guild_id: int | None
    primary_sku_id: int | None
    slug: str | None
    terms_of_service_url: str | None
    privacy_policy_url: str | None
    def __init__(self, state: ConnectionState, data: AppInfoPayload) -> None: ...
    @property
    def icon(self) -> Asset | None: ...
    @property
    def cover_image(self) -> Asset | None: ...
    @property
    def guild(self) -> Guild | None: ...

class PartialAppInfo:
    id: int
    name: str
    description: str
    rpc_origins: list[str] | None
    summary: str
    verify_key: str
    terms_of_service_url: str | None
    privacy_policy_url: str | None
    def __init__(self, *, state: ConnectionState, data: PartialAppInfoPayload) -> None: ...
    @property
    def icon(self) -> Asset | None: ...
