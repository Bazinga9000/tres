from .enums import ExpireBehaviour
from .guild import Guild
from .role import Role
from .types.integration import Integration as IntegrationPayload, IntegrationAccount as IntegrationAccountPayload, IntegrationApplication as IntegrationApplicationPayload
from .user import User
from _typeshed import Incomplete

__all__ = ['IntegrationAccount', 'IntegrationApplication', 'Integration', 'StreamIntegration', 'BotIntegration']

class IntegrationAccount:
    id: str
    name: str
    def __init__(self, data: IntegrationAccountPayload) -> None: ...

class Integration:
    guild: Incomplete
    def __init__(self, *, data: IntegrationPayload, guild: Guild) -> None: ...
    async def delete(self, *, reason: str | None = None) -> None: ...

class StreamIntegration(Integration):
    @property
    def expire_behavior(self) -> ExpireBehaviour: ...
    @property
    def role(self) -> Role | None: ...
    async def edit(self, *, expire_behaviour: ExpireBehaviour = ..., expire_grace_period: int = ..., enable_emoticons: bool = ...) -> None: ...
    synced_at: Incomplete
    async def sync(self) -> None: ...

class IntegrationApplication:
    id: int
    name: str
    icon: str | None
    description: str
    summary: str
    user: User | None
    def __init__(self, *, data: IntegrationApplicationPayload, state) -> None: ...

class BotIntegration(Integration): ...
