from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .snowflake import Snowflake as Snowflake
from .user import PartialUser as PartialUser
from _typeshed import Incomplete

StatusType: Incomplete

class PartialPresenceUpdate(TypedDict):
    user: PartialUser
    guild_id: Snowflake
    status: StatusType
    activities: list[Activity]
    client_status: ClientStatus

class ClientStatus(TypedDict, total=False):
    desktop: str
    mobile: str
    web: str

class ActivityTimestamps(TypedDict, total=False):
    start: int
    end: int

class ActivityParty(TypedDict, total=False):
    id: str
    size: list[int]

class ActivityAssets(TypedDict, total=False):
    large_image: str
    large_text: str
    small_image: str
    small_text: str

class ActivitySecrets(TypedDict, total=False):
    join: str
    spectate: str
    match: str

class ActivityEmoji(TypedDict):
    id: NotRequired[Snowflake]
    animated: NotRequired[bool]
    name: str

class ActivityButton(TypedDict):
    label: str
    url: str

ActivityType: Incomplete

class SendableActivity(TypedDict):
    url: NotRequired[str | None]
    name: str
    type: ActivityType

class _BaseActivity(SendableActivity):
    created_at: int

class Activity(_BaseActivity, total=False):
    state: str | None
    details: str | None
    timestamps: ActivityTimestamps
    assets: ActivityAssets
    party: ActivityParty
    application_id: Snowflake
    flags: int
    emoji: ActivityEmoji | None
    secrets: ActivitySecrets
    session_id: str | None
    instance: bool
    buttons: list[str]
