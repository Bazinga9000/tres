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

        draw_button_label = f'Pay Card Debt ({self.game.card_debt})' if self.game.card_debt > 0 else 'Draw a card'
        self.draw_button = Button[CardView](label=draw_button_label, style=ButtonStyle.danger)
        async def draw_callback(interaction: Interaction):
            if self.game.card_debt <= 0:
                self.game.draw_card(self.game.active_player)
                self.pass_button.disabled = False
                self.update_card_select()
                await self.game.channel.send(f'{self.game.active_player.display_name} drew a card!')
                await interaction.response.edit_message(view=self)
            else:
                self.game.draw_card(self.game.active_player, n=self.game.card_debt)
                await self.game.channel.send(f'{self.game.active_player.display_name} paid the card debt ({self.game.card_debt})!')
                self.game.card_debt = 0
                await self.end_turn_and_die(interaction)



        self.draw_button.callback = draw_callback

        self.pass_button = Button[CardView](label='Pass turn', style=ButtonStyle.blurple, disabled=True)
        async def pass_callback(interaction: Interaction):
            player = self.game.players[self.game.whose_turn]
            await self.game.channel.send(f'{player.display_name} passed their turn!')
            await self.end_turn_and_die(interaction)

        self.pass_button.callback = pass_callback

        self.play_button = Button[CardView](label='Play selected card', style=ButtonStyle.success, disabled=True)
        self.selected_card: int = -1
        self.selects: set[BaseSelect[Any]] = set()
        self.unset: set[BaseSelect[Any]] = set()
        super().__init__(self.draw_button, self.pass_button, self.play_button)
        self.card_select = self.generate_card_select()
        self.update_card_select()


    def update_card_select(self):
        self.remove_item(self.card_select.select)
        self.card_select = self.generate_card_select()
        if len(self.card_select.select.options) > 0:
            self.add_item(self.card_select.select)

    def generate_card_select(self) -> CardSelect:
        cs = CardSelect(self.game, 'Choose a card to play.', requires_playable=True)

        async def card_callback(interaction: Interaction):
            for select in self.selects:
                self.remove_item(select.select)
            self.selects.clear()
            self.unset.clear()

            card = cs.get_value()

            pile_select = PileSelect(self.game, f'Select a pile to play {card.display_name} onto.', playable_by=card)
            self.add_select(pile_select)

            on_play = card.on_select(self)

            async def play_callback(interaction: Interaction):
                player = self.game.players[self.game.whose_turn]
                card = cs.get_value()
                pile = pile_select.get_value()

                player.hand.remove_card(card)
                self.game.piles[pile].append(card)

                await on_play(interaction)
                await self.end_turn_and_die(interaction)

            self.play_button.callback = play_callback

            for option in cs.select.options:
                option.default = option.value in cs.select.values

            self.play_button.disabled = bool(self.unset)
            await interaction.response.edit_message(view=self)
        cs.select.callback = card_callback
        return cs


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

    async def end_turn_and_die(self, interaction: Interaction):
        self.stop()
        await self.game.end_turn()
        await interaction.response.defer()
        await interaction.delete_original_response()
