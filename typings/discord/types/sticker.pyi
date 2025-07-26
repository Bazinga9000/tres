from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from .user import User as User
from _typeshed import Incomplete
from typing import Literal

StickerFormatType: Incomplete

class StickerItem(TypedDict):
    id: Snowflake
    name: str
    format_type: StickerFormatType

class BaseSticker(TypedDict):
    id: Snowflake
    name: str
    description: str
    tags: str
    format_type: StickerFormatType

class StandardSticker(BaseSticker):
    type: Literal[1]
    sort_value: int
    pack_id: Snowflake

class GuildSticker(BaseSticker):
    user: NotRequired[User]
    type: Literal[2]
    available: bool
    guild_id: Snowflake
Sticker = BaseSticker | StandardSticker | GuildSticker

class StickerPack(TypedDict):
    id: Snowflake
    stickers: list[StandardSticker]
    name: str
    sku_id: Snowflake
    cover_sticker_id: Snowflake
    description: str
    banner_asset_id: Snowflake

class CreateGuildSticker(TypedDict):
    description: NotRequired[str]
    name: str
    tags: str

class EditGuildSticker(TypedDict, total=False):
    name: str
    tags: str
    description: str

class ListPremiumStickerPacks(TypedDict):
    sticker_packs: list[StickerPack]
