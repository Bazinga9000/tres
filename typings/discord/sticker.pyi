import datetime
from .asset import Asset, AssetMixin
from .enums import StickerFormatType
from .guild import Guild
from .mixins import Hashable
from .state import ConnectionState
from .types.sticker import Sticker as StickerPayload, StickerItem as StickerItemPayload, StickerPack as StickerPackPayload

__all__ = ['StickerPack', 'StickerItem', 'Sticker', 'StandardSticker', 'GuildSticker']

class StickerPack(Hashable):
    def __init__(self, *, state: ConnectionState, data: StickerPackPayload) -> None: ...
    @property
    def banner(self) -> Asset: ...

class _StickerTag(Hashable, AssetMixin):
    id: int
    format: StickerFormatType
    async def read(self) -> bytes: ...

class StickerItem(_StickerTag):
    name: str
    id: int
    format: StickerFormatType
    url: str
    def __init__(self, *, state: ConnectionState, data: StickerItemPayload) -> None: ...
    async def fetch(self) -> Sticker | StandardSticker | GuildSticker: ...

class Sticker(_StickerTag):
    def __init__(self, *, state: ConnectionState, data: StickerPayload) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class StandardSticker(Sticker):
    async def pack(self) -> StickerPack: ...

class GuildSticker(Sticker):
    def guild(self) -> Guild | None: ...
    async def edit(self, *, name: str = ..., description: str = ..., emoji: str = ..., reason: str | None = None) -> GuildSticker: ...
    async def delete(self, *, reason: str | None = None) -> None: ...
