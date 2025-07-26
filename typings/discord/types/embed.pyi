from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from _typeshed import Incomplete

class EmbedFooter(TypedDict):
    icon_url: NotRequired[str]
    proxy_icon_url: NotRequired[str]
    text: str

class EmbedField(TypedDict):
    inline: NotRequired[bool]
    name: str
    value: str

class EmbedThumbnail(TypedDict, total=False):
    url: str
    proxy_url: str
    height: int
    width: int

class EmbedVideo(TypedDict, total=False):
    url: str
    proxy_url: str
    height: int
    width: int

class EmbedImage(TypedDict, total=False):
    url: str
    proxy_url: str
    height: int
    width: int

class EmbedProvider(TypedDict, total=False):
    name: str
    url: str

class EmbedAuthor(TypedDict, total=False):
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str

EmbedType: Incomplete

class Embed(TypedDict, total=False):
    title: str
    type: EmbedType
    description: str
    url: str
    timestamp: str
    color: int
    footer: EmbedFooter
    image: EmbedImage
    thumbnail: EmbedThumbnail
    video: EmbedVideo
    provider: EmbedProvider
    author: EmbedAuthor
    fields: list[EmbedField]
