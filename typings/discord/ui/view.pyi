from ..components import Component
from ..interactions import Interaction
from ..message import Message
from ..state import ConnectionState
from ..types.components import Component as ComponentPayload
from .item import Item, ItemCallbackType
from _typeshed import Incomplete
from typing import Any, ClassVar, Sequence

__all__ = ['View']

class _ViewWeights:
    weights: list[int]
    def __init__(self, children: list[Item]) -> None: ...
    def find_open_space(self, item: Item) -> int: ...
    def add_item(self, item: Item) -> None: ...
    def remove_item(self, item: Item) -> None: ...
    def clear(self) -> None: ...

class View:
    __discord_ui_view__: ClassVar[bool]
    __view_children_items__: ClassVar[list[ItemCallbackType]]
    def __init_subclass__(cls) -> None: ...
    timeout: Incomplete
    disable_on_timeout: Incomplete
    children: list[Item]
    id: str
    parent: Interaction | None
    def __init__(self, *items: Item[View], timeout: float | None = 180.0, disable_on_timeout: bool = False) -> None: ... # STUB: CAP
    def to_components(self) -> list[dict[str, Any]]: ...
    @classmethod
    def from_message(cls, message: Message, /, *, timeout: float | None = 180.0) -> View: ...
    def add_item(self, item: Item[View]) -> None: ... # STUB: CAP
    def remove_item(self, item: Item[View]) -> None: ... # STUB: CAP
    def clear_items(self) -> None: ...
    def get_item(self, custom_id: str) -> Item | None: ...
    async def interaction_check(self, interaction: Interaction) -> bool: ...
    async def on_timeout(self) -> None: ...
    async def on_check_failure(self, interaction: Interaction) -> None: ...
    async def on_error(self, error: Exception, item: Item, interaction: Interaction) -> None: ...
    def refresh(self, components: list[Component]): ...
    def stop(self) -> None: ...
    def is_finished(self) -> bool: ...
    def is_dispatching(self) -> bool: ...
    def is_persistent(self) -> bool: ...
    async def wait(self) -> bool: ...
    def disable_all_items(self, *, exclusions: list[Item[View]] | None = None) -> None: ... # STUB: CAP
    def enable_all_items(self, *, exclusions: list[Item] | None = None) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, value) -> None: ...

class ViewStore:
    def __init__(self, state: ConnectionState) -> None: ...
    @property
    def persistent_views(self) -> Sequence[View]: ...
    def add_view(self, view: View, message_id: int | None = None): ...
    def remove_view(self, view: View): ...
    def dispatch(self, component_type: int, custom_id: str, interaction: Interaction): ...
    def is_message_tracked(self, message_id: int): ...
    def remove_message_tracking(self, message_id: int) -> View | None: ...
    def update_from_message(self, message_id: int, components: list[ComponentPayload]): ...
