from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .channel import ChannelType as ChannelType
from .components import Component as Component
from .embed import Embed as Embed
from .emoji import PartialEmoji as PartialEmoji
from .interactions import InteractionMetadata as InteractionMetadata, MessageInteraction as MessageInteraction
from .member import Member as Member, UserWithMember as UserWithMember
from .poll import Poll as Poll
from .snowflake import Snowflake as Snowflake, SnowflakeList as SnowflakeList
from .sticker import StickerItem as StickerItem
from .threads import Thread as Thread
from .user import User as User
from _typeshed import Incomplete

class ChannelMention(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    type: ChannelType
    name: str

class Reaction(TypedDict):
    count: int
    me: bool
    emoji: PartialEmoji
    burst: bool
    me_burst: bool
    burst_colors: list[str]
    count_details: ReactionCountDetails

class ReactionCountDetails(TypedDict):
    normal: int
    burst: int

class Attachment(TypedDict):
    height: NotRequired[int | None]
    width: NotRequired[int | None]
    content_type: NotRequired[str]
    description: NotRequired[str]
    spoiler: NotRequired[bool]
    id: Snowflake
    filename: str
    size: int
    url: str
    proxy_url: str
    duration_secs: NotRequired[float]
    waveform: NotRequired[str]
    flags: NotRequired[int]
    title: NotRequired[str]

MessageActivityType: Incomplete

class MessageActivity(TypedDict):
    type: MessageActivityType
    party_id: str

class MessageApplication(TypedDict):
    cover_image: NotRequired[str]
    id: Snowflake
    description: str
    icon: str | None
    name: str

class MessageReference(TypedDict, total=False):
    message_id: Snowflake
    channel_id: Snowflake
    guild_id: Snowflake
    fail_if_not_exists: bool

MessageType: Incomplete

class Message(TypedDict):
    guild_id: NotRequired[Snowflake]
    member: NotRequired[Member]
    mention_channels: NotRequired[list[ChannelMention]]
    reactions: NotRequired[list[Reaction]]
    nonce: NotRequired[int | str]
    webhook_id: NotRequired[Snowflake]
    activity: NotRequired[MessageActivity]
    application: NotRequired[MessageApplication]
    application_id: NotRequired[Snowflake]
    message_reference: NotRequired[MessageReference]
    flags: NotRequired[int]
    sticker_items: NotRequired[list[StickerItem]]
    referenced_message: NotRequired[Message | None]
    interaction: NotRequired[MessageInteraction]
    interaction_metadata: NotRequired[InteractionMetadata]
    components: NotRequired[list[Component]]
    thread: NotRequired[Thread | None]
    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: str
    edited_timestamp: str | None
    tts: bool
    mention_everyone: bool
    mentions: list[UserWithMember]
    mention_roles: SnowflakeList
    attachments: list[Attachment]
    embeds: list[Embed]
    pinned: bool
    type: MessageType
    poll: Poll

AllowedMentionType: Incomplete

class AllowedMentions(TypedDict):
    parse: list[AllowedMentionType]
    roles: SnowflakeList
    users: SnowflakeList
    replied_user: bool

class MessageCall(TypedDict):
    participants: SnowflakeList
    ended_timestamp: NotRequired[str]
