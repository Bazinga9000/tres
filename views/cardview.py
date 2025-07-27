from typing import TYPE_CHECKING, Any

from discord import ButtonStyle
from discord.interactions import Interaction
from discord.ui import Button, View

from .select.base import BaseSelect
from .select.card import CardSelect
from .select.pile import PileSelect

if TYPE_CHECKING:
    from game import Game
else:
    Game = Any


class CardView(View):
    def __init__(self, game: Game):
        self.game = game
        
        self.draw_button = Button[CardView](label='Draw a card', style=ButtonStyle.danger)
        async def draw_callback(interaction: Interaction):
            player = self.game.players[self.game.whose_turn]
            self.game.draw_card(player)
            self.pass_button.disabled = False
            await self.game.channel.send(f'{player.display_name} drew a card!')
            await interaction.response.edit_message(view=self)
        self.draw_button.callback = draw_callback
        
        self.pass_button = Button[CardView](label='Pass turn', style=ButtonStyle.blurple, disabled=True)
        async def pass_callback(interaction: Interaction):
            player = self.game.players[self.game.whose_turn]
            await self.game.channel.send(f'{player.display_name} passed their turn!')
            await self.game.end_turn()
            await interaction.response.defer()
            await interaction.delete_original_response()
        self.pass_button.callback = pass_callback
        
        self.play_button = Button[CardView](label='Play selected card', style=ButtonStyle.success, disabled=True)
        
        self.card_select = CardSelect(game, 'Choose a card to play.', requires_playable=True)
        async def card_callback(interaction: Interaction):
            for select in self.selects:
                self.remove_item(select.select)
            self.selects.clear()
            self.unset.clear()
            
            card = self.card_select.get_value()
            
            pile_select = PileSelect(game, f'Select a pile to play {card.display_name} onto.', playable_by=card)
            self.add_select(pile_select)
            
            on_play = card.on_select(self)
            
            async def play_callback(interaction: Interaction):
                player = self.game.players[self.game.whose_turn]
                hand = self.game.hands[player]
                card = self.card_select.get_value()
                pile = pile_select.get_value()
                
                hand.remove_card(card)
                game.piles[pile].append(card)
                
                await on_play(interaction)
                await interaction.response.defer()
                await interaction.delete_original_response()
                await self.game.end_turn()
            
            self.play_button.callback = play_callback
            
            for option in self.card_select.select.options:
                option.default = option.value in self.card_select.select.values
            
            self.play_button.disabled = bool(self.unset)
            await interaction.response.edit_message(view=self)
        self.card_select.select.callback = card_callback
        
        self.selected_card: int = -1
        self.selects: set[BaseSelect[Any]] = set()
        self.unset: set[BaseSelect[Any]] = set()
        super().__init__(self.draw_button, self.pass_button, self.play_button, self.card_select.select)
    
    
    def add_select[T](self, select: BaseSelect[T]):
        if select in self.selects:
            return self
        
        async def callback(interaction: Interaction):
            for option in select.select.options:
                option.default = option.value in select.select.values
            self.unset.discard(select)
            if not self.unset:
                self.play_button.disabled = False
            await interaction.response.edit_message(view=self)
        select.select.callback = callback
        
        self.play_button.disabled = True
        self.selects.add(select)
        self.unset.add(select)
        return self.add_item(select.select)
