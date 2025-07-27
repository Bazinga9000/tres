from .emoji import Emoji
from .enums import ButtonStyle, ChannelType, ComponentType, InputTextStyle
from .partial_emoji import PartialEmoji
from .types.components import ActionRow as ActionRowPayload, ButtonComponent as ButtonComponentPayload, Component as ComponentPayload, InputText as InputTextComponentPayload, SelectMenu as SelectMenuPayload, SelectOption as SelectOptionPayload
from _typeshed import Incomplete
from typing import Any, ClassVar, TypeVar

__all__ = ['Component', 'ActionRow', 'Button', 'SelectMenu', 'SelectOption', 'InputText']

C = TypeVar('C', bound='Component')

class Component:
    __repr_info__: ClassVar[tuple[str, ...]]
    type: ComponentType
    def to_dict(self) -> dict[str, Any]: ...

class ActionRow(Component):
    __repr_info__: ClassVar[tuple[str, ...]]
    type: ComponentType
    children: list[Component]
    def __init__(self, data: ComponentPayload) -> None: ...
    def to_dict(self) -> ActionRowPayload: ...

class InputText(Component):
    __repr_info__: ClassVar[tuple[str, ...]]
    type: Incomplete
    style: InputTextStyle
    custom_id: Incomplete
    label: str
    placeholder: str | None
    min_length: int | None
    max_length: int | None
    required: bool
    value: str | None
    def __init__(self, data: InputTextComponentPayload) -> None: ...
    def to_dict(self) -> InputTextComponentPayload: ...

class Button(Component):
    __repr_info__: ClassVar[tuple[str, ...]]
    type: ComponentType
    style: ButtonStyle
    custom_id: str | None
    url: str | None
    disabled: bool
    label: str | None
    emoji: PartialEmoji | None
    sku_id: str | None
    def __init__(self, data: ButtonComponentPayload) -> None: ...
    def to_dict(self) -> ButtonComponentPayload: ...

class SelectMenu(Component):
    __repr_info__: ClassVar[tuple[str, ...]]
    type: Incomplete
    custom_id: str
    placeholder: str | None
    min_values: int
    max_values: int
    disabled: bool
    options: list[SelectOption]
    channel_types: list[ChannelType]
    def __init__(self, data: SelectMenuPayload) -> None: ...
    def to_dict(self) -> SelectMenuPayload: ...

class SelectOption:
    label: str # STUB: CAP
    value: Incomplete
    description: str # STUB: CAP
    default: bool # STUB: CAP
    def __init__(self, *, label: str, value: str = ..., description: str | None = None, emoji: str | Emoji | PartialEmoji | None = None, default: bool = False) -> None: ...
    @property
    def emoji(self) -> str | Emoji | PartialEmoji | None: ...
    @emoji.setter
    def emoji(self, value) -> None: ...
    @classmethod
    def from_dict(cls, data: SelectOptionPayload) -> SelectOption: ...
    def to_dict(self) -> SelectOptionPayload: ...
