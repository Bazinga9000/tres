import datetime
from .colour import Colour
from .enums import ActivityType
from .partial_emoji import PartialEmoji
from .types.activity import Activity as ActivityPayload, ActivityAssets, ActivityParty, ActivityTimestamps
from typing import Any, overload

__all__ = ['BaseActivity', 'Activity', 'Streaming', 'Game', 'Spotify', 'CustomActivity']

class BaseActivity:
    def __init__(self, **kwargs) -> None: ...
    @property
    def created_at(self) -> datetime.datetime | None: ...
    def to_dict(self) -> ActivityPayload: ...

class Activity(BaseActivity):
    state: str | None
    details: str | None
    timestamps: ActivityTimestamps
    assets: ActivityAssets
    party: ActivityParty
    application_id: int | None
    url: str | None
    flags: int
    sync_id: str | None
    session_id: str | None
    buttons: list[str]
    type: ActivityType
    name: str | None
    emoji: PartialEmoji | None
    def __init__(self, **kwargs) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    @property
    def start(self) -> datetime.datetime | None: ...
    @property
    def end(self) -> datetime.datetime | None: ...
    @property
    def large_image_url(self) -> str | None: ...
    @property
    def small_image_url(self) -> str | None: ...
    @property
    def large_image_text(self) -> str | None: ...
    @property
    def small_image_text(self) -> str | None: ...

class Game(BaseActivity):
    name: str
    def __init__(self, name: str, **extra) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def start(self) -> datetime.datetime | None: ...
    @property
    def end(self) -> datetime.datetime | None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Streaming(BaseActivity):
    platform: str | None
    name: str | None
    game: str | None
    url: str
    details: str | None
    assets: ActivityAssets
    def __init__(self, *, name: str | None, url: str, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def twitch_name(self) -> str | None: ...
    def to_dict(self) -> dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Spotify:
    def __init__(self, **data) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def created_at(self) -> datetime.datetime | None: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    def to_dict(self) -> dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def title(self) -> str: ...
    @property
    def artists(self) -> list[str]: ...
    @property
    def artist(self) -> str: ...
    @property
    def album(self) -> str: ...
    @property
    def album_cover_url(self) -> str: ...
    @property
    def track_id(self) -> str: ...
    @property
    def track_url(self) -> str: ...
    @property
    def start(self) -> datetime.datetime: ...
    @property
    def end(self) -> datetime.datetime: ...
    @property
    def duration(self) -> datetime.timedelta: ...
    @property
    def party_id(self) -> str: ...

class CustomActivity(BaseActivity):
    name: str | None
    state: str | None
    emoji: PartialEmoji | None
    def __init__(self, name: str | None, *, emoji: PartialEmoji | None = None, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    def to_dict(self) -> dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
ActivityTypes = Activity | Game | CustomActivity | Streaming | Spotify
