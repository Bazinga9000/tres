from typing import Callable, overload

from discord.interactions import Interaction
from .cardview import CardView
from .select.base import BaseSelect
from .select.card import CardSelect
from .select.color import ColorSelect
from .select.player import PlayerSelect

type V[*T] = VarView[*T]
class VarView[*Ts]:
    @overload
    def __init__(self: V[()], view: CardView, /) -> None:
        ...
    
    @overload
    def __init__[*H, T](self: V[*H, T], data: tuple[V[*H], BaseSelect[T]], /) -> None:
        ...
    
    def __init__[*H, T](self: V[*H, T], data_or_view: CardView | tuple[V[*H], BaseSelect[T]]):
        match data_or_view:
            case CardView() as view:
                self.view = view
                self.data = ()
            case (head, tail):
                self.view = head.view
                self.view.add_select(tail)
                self.data = (head, tail)
    
    def get_values(self) -> tuple[*Ts]:
        vals = ()
        if self.data:
            head, tail = self.data
            vals = (*head.get_values(), tail.get_value())
        return vals # type: ignore # necessary evil
    
    def add_player(self):
        return VarView((self, PlayerSelect(self.view.game)))
    
    def add_card(self):
        return VarView((self, CardSelect(self.view.game)))
    
    def add_color(self):
        return VarView((self, ColorSelect(self.view.game)))
    
    def add_callback(self, callback: Callable[[*Ts], None]):
        async def wrapped(interaction: Interaction):
            values = self.get_values()
            callback(*values)
            await interaction.response.edit_message(content='hi', view=None)
        self.view.play_button.callback = wrapped
        return ...
