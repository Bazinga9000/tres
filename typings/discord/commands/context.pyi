import discord.abc
from .. import Bot
from ..client import ClientUser
from ..cog import Cog
from ..guild import Guild
from ..interactions import InteractionChannel
from ..member import Member
from ..message import Message
from ..permissions import Permissions
from ..user import User
from functools import cached_property # STUB: CAP
from ..voice_client import VoiceClient
from ..webhook import WebhookMessage
from .core import ApplicationCommand, Option
from _typeshed import Incomplete
from discord.interactions import Interaction, InteractionMessage, InteractionResponse
from discord.webhook.async_ import Webhook
from typing import Any, Awaitable, Callable, TypeVar
from typing_extensions import ParamSpec

__all__ = ['ApplicationContext', 'AutocompleteContext']

T = TypeVar('T')
CogT = TypeVar('CogT', bound='Cog')
P = ParamSpec('P')

class ApplicationContext(discord.abc.Messageable):
    bot: Incomplete
    interaction: Incomplete
    command: ApplicationCommand
    focused: Option
    value: str
    options: dict
    def __init__(self, bot: Bot, interaction: Interaction) -> None: ...
    async def invoke(self, command: ApplicationCommand[CogT, P, T], /, *args: P.args, **kwargs: P.kwargs) -> T: ...
    @cached_property
    def channel(self) -> InteractionChannel | None: ...
    @cached_property
    def channel_id(self) -> int | None: ...
    @cached_property
    def guild(self) -> Guild | None: ...
    @cached_property
    def guild_id(self) -> int | None: ...
    @cached_property
    def locale(self) -> str | None: ...
    @cached_property
    def guild_locale(self) -> str | None: ...
    @cached_property
    def app_permissions(self) -> Permissions: ...
    @cached_property
    def me(self) -> Member | ClientUser | None: ...
    @cached_property
    def message(self) -> Message | None: ...
    @cached_property
    def user(self) -> Member | User: ...
    author: Member | User
    @property
    def voice_client(self) -> VoiceClient | None: ...
    @cached_property
    def response(self) -> InteractionResponse: ...
    @property
    def selected_options(self) -> list[dict[str, Any]] | None: ...
    @property
    def unselected_options(self) -> list[Option] | None: ...
    @property
    def send_modal(self) -> Callable[..., Awaitable[Interaction]]: ...
    @property
    def respond(self, *args, **kwargs) -> Callable[..., Awaitable[Interaction | WebhookMessage]]: ...
    @property
    def send_response(self) -> Callable[..., Awaitable[Interaction]]: ...
    @property
    def send_followup(self) -> Callable[..., Awaitable[WebhookMessage]]: ...
    @property
    def defer(self) -> Callable[..., Awaitable[None]]: ...
    @property
    def followup(self) -> Webhook: ...
    async def delete(self, *, delay: float | None = None) -> None: ...
    @property
    def edit(self) -> Callable[..., Awaitable[InteractionMessage]]: ...
    @property
    def cog(self) -> Cog | None: ...

class AutocompleteContext:
    bot: Incomplete
    interaction: Incomplete
    command: ApplicationCommand
    focused: Option
    value: str
    options: dict
    def __init__(self, bot: Bot, interaction: Interaction) -> None: ...
    @property
    def cog(self) -> Cog | None: ...
