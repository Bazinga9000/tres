from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .member import MemberWithUser as MemberWithUser
from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete

SupportedModes: Incomplete

class _VoiceState(TypedDict):
    member: NotRequired[MemberWithUser]
    self_stream: NotRequired[bool]
    user_id: Snowflake
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_video: bool
    suppress: bool

class GuildVoiceState(_VoiceState):
    channel_id: Snowflake

class VoiceState(_VoiceState, total=False):
    channel_id: Snowflake | None
    guild_id: Snowflake

class VoiceRegion(TypedDict):
    id: str
    name: str
    vip: bool
    optimal: bool
    deprecated: bool
    custom: bool

class VoiceServerUpdate(TypedDict):
    token: str
    guild_id: Snowflake
    endpoint: str | None

class VoiceIdentify(TypedDict):
    server_id: Snowflake
    user_id: Snowflake
    session_id: str
    token: str

class VoiceReady(TypedDict):
    ssrc: int
    ip: str
    port: int
    modes: list[SupportedModes]
    heartbeat_interval: int
