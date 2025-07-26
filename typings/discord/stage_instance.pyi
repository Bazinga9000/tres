from .channel import StageChannel
from .enums import StagePrivacyLevel
from .guild import Guild
from .mixins import Hashable
from .state import ConnectionState
from .types.channel import StageInstance as StageInstancePayload
from _typeshed import Incomplete

__all__ = ['StageInstance']

class StageInstance(Hashable):
    guild: Incomplete
    def __init__(self, *, state: ConnectionState, guild: Guild, data: StageInstancePayload) -> None: ...
    def channel(self) -> StageChannel | None: ...
    def is_public(self) -> bool: ...
    async def edit(self, *, topic: str = ..., privacy_level: StagePrivacyLevel = ..., reason: str | None = None) -> None: ...
    async def delete(self, *, reason: str | None = None) -> None: ...
