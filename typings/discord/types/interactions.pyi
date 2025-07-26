from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from ..interactions import InteractionChannel as InteractionChannel
from ..permissions import Permissions as Permissions
from .channel import ChannelType as ChannelType
from .components import Component as Component, ComponentType as ComponentType
from .embed import Embed as Embed
from .member import Member as Member
from .message import AllowedMentions as AllowedMentions, Attachment as Attachment, Message as Message
from .monetization import Entitlement as Entitlement
from .role import Role as Role
from .snowflake import Snowflake as Snowflake
from .user import User as User
from _typeshed import Incomplete
from typing import Literal

ApplicationCommandType: Incomplete

class ApplicationCommand(TypedDict):
    id: Snowflake
    type: NotRequired[ApplicationCommandType]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    name_localizations: NotRequired[dict[str, str] | None]
    description: str
    description_localizations: NotRequired[dict[str, str] | None]
    options: NotRequired[list[ApplicationCommandOption]]
    default_member_permissions: str | None
    dm_permission: NotRequired[bool]
    default_permission: NotRequired[bool | None]
    nsfw: NotRequired[bool]
    version: Snowflake

ApplicationCommandOptionType: Incomplete

class ApplicationCommandOption(TypedDict):
    type: ApplicationCommandOptionType
    name: str
    name_localizations: NotRequired[dict[str, str] | None]
    description: str
    description_localizations: NotRequired[dict[str, str] | None]
    required: bool
    options: NotRequired[list[ApplicationCommandOption]]
    choices: NotRequired[list[ApplicationCommandOptionChoice]]
    channel_types: NotRequired[list[ChannelType]]
    min_value: NotRequired[int | float]
    max_value: NotRequired[int | float]
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    autocomplete: NotRequired[bool]

class ApplicationCommandOptionChoice(TypedDict):
    name: str
    name_localizations: NotRequired[dict[str, str] | None]
    value: str | int

ApplicationCommandPermissionType: Incomplete

class ApplicationCommandPermissions(TypedDict):
    id: Snowflake
    type: ApplicationCommandPermissionType
    permission: bool

class BaseGuildApplicationCommandPermissions(TypedDict):
    permissions: list[ApplicationCommandPermissions]

class PartialGuildApplicationCommandPermissions(BaseGuildApplicationCommandPermissions):
    id: Snowflake

class GuildApplicationCommandPermissions(PartialGuildApplicationCommandPermissions):
    application_id: Snowflake
    guild_id: Snowflake

InteractionType: Incomplete

class _ApplicationCommandInteractionDataOption(TypedDict):
    name: str

class _ApplicationCommandInteractionDataOptionSubcommand(_ApplicationCommandInteractionDataOption):
    type: Literal[1, 2]
    options: list[ApplicationCommandInteractionDataOption]

class _ApplicationCommandInteractionDataOptionString(_ApplicationCommandInteractionDataOption):
    type: Literal[3]
    value: str

class _ApplicationCommandInteractionDataOptionInteger(_ApplicationCommandInteractionDataOption):
    type: Literal[4]
    value: int

class _ApplicationCommandInteractionDataOptionBoolean(_ApplicationCommandInteractionDataOption):
    type: Literal[5]
    value: bool

class _ApplicationCommandInteractionDataOptionSnowflake(_ApplicationCommandInteractionDataOption):
    type: Literal[6, 7, 8, 9, 11]
    value: Snowflake

class _ApplicationCommandInteractionDataOptionNumber(_ApplicationCommandInteractionDataOption):
    type: Literal[10]
    value: float

ApplicationCommandInteractionDataOption: Incomplete

class ApplicationCommandResolvedPartialChannel(TypedDict):
    id: Snowflake
    type: ChannelType
    permissions: str
    name: str

class ApplicationCommandInteractionDataResolved(TypedDict, total=False):
    users: dict[Snowflake, User]
    members: dict[Snowflake, Member]
    roles: dict[Snowflake, Role]
    channels: dict[Snowflake, ApplicationCommandResolvedPartialChannel]
    attachments: dict[Snowflake, Attachment]

class ApplicationCommandInteractionData(TypedDict):
    options: NotRequired[list[ApplicationCommandInteractionDataOption]]
    resolved: NotRequired[ApplicationCommandInteractionDataResolved]
    target_id: NotRequired[Snowflake]
    type: NotRequired[ApplicationCommandType]
    id: Snowflake
    name: str

class ComponentInteractionData(TypedDict):
    values: NotRequired[list[str]]
    custom_id: str
    component_type: ComponentType
InteractionData = ApplicationCommandInteractionData | ComponentInteractionData

class Interaction(TypedDict):
    data: NotRequired[InteractionData]
    guild_id: NotRequired[Snowflake]
    channel_id: NotRequired[Snowflake]
    channel: NotRequired[InteractionChannel]
    member: NotRequired[Member]
    user: NotRequired[User]
    message: NotRequired[Message]
    locale: NotRequired[str]
    guild_locale: NotRequired[str]
    app_permissions: NotRequired[Permissions]
    id: Snowflake
    application_id: Snowflake
    type: InteractionType
    token: str
    version: int
    entitlements: list[Entitlement]
    authorizing_integration_owners: AuthorizingIntegrationOwners
    context: InteractionContextType

class InteractionMetadata(TypedDict):
    id: Snowflake
    type: InteractionType
    user_id: Snowflake
    authorizing_integration_owners: AuthorizingIntegrationOwners
    original_response_message_id: NotRequired[Snowflake]
    interacted_message_id: NotRequired[Snowflake]
    triggering_interaction_metadata: NotRequired[InteractionMetadata]

class InteractionApplicationCommandCallbackData(TypedDict, total=False):
    tts: bool
    content: str
    embeds: list[Embed]
    allowed_mentions: AllowedMentions
    flags: int
    components: list[Component]

InteractionResponseType: Incomplete

class InteractionResponse(TypedDict):
    data: NotRequired[InteractionApplicationCommandCallbackData]
    type: InteractionResponseType

class MessageInteraction(TypedDict):
    id: Snowflake
    type: InteractionType
    name: str
    user: User

class EditApplicationCommand(TypedDict):
    description: NotRequired[str]
    options: NotRequired[list[ApplicationCommandOption] | None]
    type: NotRequired[ApplicationCommandType]
    name: str
    default_permission: bool

InteractionContextType: Incomplete
ApplicationIntegrationType: Incomplete
AuthorizingIntegrationOwners: Incomplete
