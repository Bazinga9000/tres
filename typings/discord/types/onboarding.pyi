from .._typed_dict import NotRequired as NotRequired
from .emoji import Emoji as Emoji
from .snowflake import Snowflake as Snowflake, SnowflakeList as SnowflakeList
from _typeshed import Incomplete
from typing import TypedDict

PromptType: Incomplete
OnboardingMode: Incomplete

class Onboarding(TypedDict):
    guild_id: Snowflake
    prompts: list[OnboardingPrompt]
    default_channel_ids: SnowflakeList
    enabled: bool
    mode: OnboardingMode

class OnboardingPrompt(TypedDict):
    id: Snowflake
    type: PromptType
    options: list[PromptOption]
    title: str
    single_select: bool
    required: bool
    in_onboarding: bool

class PromptOption(TypedDict):
    id: Snowflake
    channel_ids: SnowflakeList
    role_ids: SnowflakeList
    emoji: NotRequired[Emoji]
    emoji_id: NotRequired[Snowflake]
    emoji_name: NotRequired[str]
    emoji_animated: NotRequired[bool]
    title: str
    description: str | None
