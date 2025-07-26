import datetime
from .activity import BaseActivity, Spotify
from .enums import Status
from .invite import Invite
from .state import ConnectionState
from .types.widget import Widget as WidgetPayload, WidgetMember as WidgetMemberPayload
from .user import BaseUser
from typing import Any

__all__ = ['WidgetChannel', 'WidgetMember', 'Widget']

class WidgetChannel:
    id: int
    name: str
    position: int
    def __init__(self, id: int, name: str, position: int) -> None: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class WidgetMember(BaseUser):
    activity: BaseActivity | Spotify | None
    nick: str | None
    status: Status
    deafened: bool | None
    muted: bool | None
    suppress: bool | None
    connected_channel: WidgetChannel | None
    def __init__(self, *, state: ConnectionState, data: WidgetMemberPayload, connected_channel: WidgetChannel | None = None) -> None: ...
    @property
    def display_name(self) -> str: ...

class Widget:
    name: str
    id: int
    channels: list[WidgetChannel]
    members: list[WidgetMember]
    def __init__(self, *, state: ConnectionState, data: WidgetPayload) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def json_url(self) -> str: ...
    @property
    def invite_url(self) -> str: ...
    async def fetch_invite(self, *, with_counts: bool = True) -> Invite: ...
