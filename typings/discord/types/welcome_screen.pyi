from .snowflake import Snowflake as Snowflake
from typing import TypedDict

class WelcomeScreen(TypedDict):
    description: str
    welcome_channels: list[WelcomeScreenChannel]

class WelcomeScreenChannel(TypedDict):
    channel_id: Snowflake
    description: str
    emoji_id: Snowflake | None
    emoji_name: str | None
