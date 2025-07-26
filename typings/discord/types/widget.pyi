from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .activity import Activity as Activity
from .snowflake import Snowflake as Snowflake
from .user import User as User

class WidgetChannel(TypedDict):
    id: Snowflake
    name: str
    position: int

class WidgetMember(User, total=False):
    nick: str
    game: Activity
    status: str
    avatar_url: str
    deaf: bool
    self_deaf: bool
    mute: bool
    self_mute: bool
    suppress: bool

class Widget(TypedDict):
    channels: NotRequired[list[WidgetChannel]]
    members: NotRequired[list[WidgetMember]]
    presence_count: NotRequired[int]
    id: Snowflake
    name: str
    instant_invite: str

class WidgetSettings(TypedDict):
    enabled: bool
    channel_id: Snowflake | None
