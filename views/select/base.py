from typing import override
from discord import Interaction
from discord.ui import Select, View

from util.event import Event


class BaseSelect(Select[View]):
    def __init__(self):
        super().__init__()
        self.on_select = Event[bool]()
    
    @property
    @override
    def values(self) -> list[str]:
        return [str(value) for value in super().values or [option.value for option in self.options if option.default]]
    
    async def callback(self, interaction: Interaction):
        for option in self.options:
            option.default = option.value in self.values
        self.on_select(self.has_valid_selection())
        await interaction.response.edit_message(view=self.view)
    
    def has_valid_selection(self) -> bool:
        return self.min_values <= len(self.values) <= self.max_values
    
    def get_raw_value(self) -> str:
        if not self.values:
            raise ValueError('No selection.')
        return self.values[0]
