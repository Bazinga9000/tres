from .abc import Snowflake
from .channel import ForumChannel, TextChannel, VoiceChannel
from .emoji import Emoji
from .enums import OnboardingMode, PromptType
from .guild import Guild
from .object import Object
from .partial_emoji import PartialEmoji
from .types.onboarding import Onboarding as OnboardingPayload, OnboardingPrompt as OnboardingPromptPayload, PromptOption as PromptOptionPayload
from .utils import cached_property
from _typeshed import Incomplete

__all__ = ['Onboarding', 'OnboardingPrompt', 'PromptOption']

class PromptOption:
    id: int
    title: str
    channels: list[Snowflake]
    roles: list[Snowflake]
    description: str | None
    emoji: Emoji | PartialEmoji | None
    def __init__(self, title: str, channels: list[Snowflake] | None = None, roles: list[Snowflake] | None = None, description: str | None = None, emoji: Emoji | PartialEmoji | None = None, id: int | None = None) -> None: ...
    def to_dict(self) -> PromptOptionPayload: ...

class OnboardingPrompt:
    id: int
    type: PromptType
    options: list[PromptOption]
    title: str
    single_select: bool
    required: bool
    in_onboarding: bool
    def __init__(self, type: PromptType, title: str, options: list[PromptOption], single_select: bool, required: bool, in_onboarding: bool, id: int | None = None) -> None: ...
    def to_dict(self) -> OnboardingPromptPayload: ...

class Onboarding:
    guild: Incomplete
    def __init__(self, data: OnboardingPayload, guild: Guild) -> None: ...
    @cached_property
    def default_channels(self) -> list[TextChannel | ForumChannel | VoiceChannel | Object]: ...
    async def edit(self, *, prompts: list[OnboardingPrompt] | None = ..., default_channels: list[Snowflake] | None = ..., enabled: bool | None = ..., mode: OnboardingMode | None = ..., reason: str | None = ...) -> Onboarding: ...
    async def add_prompt(self, type: PromptType, title: str, options: list[PromptOption], single_select: bool, required: bool, in_onboarding: bool, *, reason: str | None = None): ...
    async def append_prompt(self, prompt: OnboardingPrompt, *, reason: str | None = None): ...
    def get_prompt(self, id: int): ...
    async def delete_prompt(self, id: int, *, reason: str | None = ...): ...
