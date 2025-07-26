from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete

SKUType: Incomplete
EntitlementType: Incomplete
OwnerType: Incomplete

class SKU(TypedDict):
    id: Snowflake
    type: SKUType
    application_id: Snowflake
    name: str
    slug: str
    flags: int

class Entitlement(TypedDict):
    id: Snowflake
    sku_id: Snowflake
    application_id: Snowflake
    user_id: NotRequired[Snowflake]
    type: EntitlementType
    deleted: bool
    starts_at: NotRequired[str]
    ends_at: NotRequired[str]
    guild_id: NotRequired[Snowflake]

class CreateTestEntitlementPayload(TypedDict):
    sku_id: Snowflake
    owner_id: Snowflake
    owner_type: OwnerType
