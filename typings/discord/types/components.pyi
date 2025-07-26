from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from .channel import ChannelType as ChannelType
from .emoji import PartialEmoji as PartialEmoji
from .snowflake import Snowflake as Snowflake
from _typeshed import Incomplete
from typing import Literal

ComponentType: Incomplete
ButtonStyle: Incomplete
InputTextStyle: Incomplete

class ActionRow(TypedDict):
    type: Literal[1]
    components: list[Component]

class ButtonComponent(TypedDict):
    custom_id: NotRequired[str]
    url: NotRequired[str]
    disabled: NotRequired[bool]
    emoji: NotRequired[PartialEmoji]
    label: NotRequired[str]
    type: Literal[2]
    style: ButtonStyle
    sku_id: Snowflake

class InputText(TypedDict):
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    required: NotRequired[bool]
    placeholder: NotRequired[str]
    value: NotRequired[str]
    type: Literal[4]
    style: InputTextStyle
    custom_id: str
    label: str

class SelectOption(TypedDict):
    description: NotRequired[str]
    emoji: NotRequired[PartialEmoji]
    label: str
    value: str
    default: bool

class SelectMenu(TypedDict):
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]
    channel_types: NotRequired[list[ChannelType]]
    options: NotRequired[list[SelectOption]]
    type: Literal[3, 5, 6, 7, 8]
    custom_id: str
Component = ActionRow | ButtonComponent | SelectMenu | InputText
