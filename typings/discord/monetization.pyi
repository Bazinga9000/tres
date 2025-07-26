from .enums import EntitlementType, SKUType
from .flags import SKUFlags
from .mixins import Hashable
from .state import ConnectionState
from .types.monetization import Entitlement as EntitlementPayload, SKU as SKUPayload
from .utils import MISSING
from datetime import datetime

__all__ = ['SKU', 'Entitlement']

class SKU(Hashable):
    id: int
    type: SKUType
    application_id: int
    name: str
    slug: str
    flags: SKUFlags
    def __init__(self, *, data: SKUPayload) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def url(self) -> str: ...

class Entitlement(Hashable):
    id: int
    sku_id: int
    application_id: int
    user_id: int | MISSING
    type: EntitlementType
    deleted: bool
    starts_at: datetime | MISSING
    ends_at: datetime | MISSING
    guild_id: int | MISSING
    consumed: bool
    def __init__(self, *, data: EntitlementPayload, state: ConnectionState) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    async def consume(self) -> None: ...
    async def delete(self) -> None: ...
