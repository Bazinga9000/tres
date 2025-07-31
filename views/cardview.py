from typing import TYPE_CHECKING, Any, override
from uuid import UUID

from discord import ButtonStyle, SelectOption
from discord.interactions import Interaction
from discord.ui import Button, Item, View

from .select.base import BaseSelect
from .select.typed import TypedSelect

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
                self.remove_item(self.card_select)
                self.update_card_select(selected=self.card_select.values)
                await self.game.channel.send(f'{self.game.active_player.display_name} drew a card!')
                await interaction.response.edit_message(view=self)
            else:
                self.game.draw_card(self.game.active_player, n=self.game.card_debt)
                await self.game.channel.send(f'{self.game.active_player.display_name} paid the card debt ({self.game.card_debt})!')
                self.game.card_debt = 0
                await self.end_turn_and_die(interaction)
        self.draw_button.callback   = draw_callback

        self.pass_button = Button[CardView](label='Pass turn', style=ButtonStyle.blurple, disabled=True)
        async def pass_callback(interaction: Interaction):
            player = self.game.players[self.game.whose_turn]
            await self.game.channel.send(f'{player.display_name} passed their turn!')
            await self.end_turn_and_die(interaction)
        self.pass_button.callback = pass_callback

        self.play_button = Button[CardView](label='Play selected card', style=ButtonStyle.success, disabled=True)
        self.selected_card: int = -1
        self.selects: set[BaseSelect] = set()
        self.unset: set[BaseSelect] = set()
        super().__init__(self.draw_button, self.pass_button, self.play_button)
        self.update_card_select()

    def update_card_select(self, *, selected: list[str] | None = None):
        # TODO: this is code duplication from argbuilder because there are no longer reusable classes for selects
        def converter(value: str):
            card = self.game.active_player.hand.lookup_card(UUID(value))
            if not card:
                raise ValueError("Selected card index out of range.")
            return card
        card_select = TypedSelect(converter)
        card_select.placeholder = 'Choose a card to play.'
        card_select.options = [
            SelectOption(
                label=card.display_name,
                value=str(card.uuid),
                default=str(card.uuid) in (selected or [])
            )
            for card in self.game.active_player.hand.sorted()
            if card.playable_piles(self.game)
        ]

        async def card_callback(interaction: Interaction):
            for select in self.selects:
                self.remove_item(select)
            self.selects.clear()
            self.unset.clear()

            card = card_select.get_value()

            # TODO: also code duplication
            def converter(value: str):
                pile = int(value)
                if not 0 <= pile < len(self.game.piles):
                    raise ValueError('Selected pile index out of range.')
                return pile
            pile_select = TypedSelect(converter)
            pile_select.placeholder = f'Select a pile to play {card.display_name} onto.'
            pile_select.options = [
                SelectOption(label=f'Pile #{i + 1}', value=str(i))
                for i in range(len(self.game.piles))
                if card.can_play(self.game, i)
            ]
            self.add_item(pile_select)

            on_play = card.args.compile(self.game, self)

            async def play_callback(interaction: Interaction):
                player = self.game.players[self.game.whose_turn]
                card = card_select.get_value()
                pile = pile_select.get_value()

                player.hand.remove_card(card)
                self.game.piles[pile].append(card)

                on_play()
                await self.end_turn_and_die(interaction)

            self.play_button.callback = play_callback

            for option in card_select.options:
                option.default = option.value in card_select.values

            self.play_button.disabled = bool(self.unset)
            await interaction.response.edit_message(view=self)
        card_select.callback = card_callback

        if len(card_select.options) > 0:
            self.add_item(card_select)
            self.selects.remove(card_select)

        self.card_select = card_select
        return card_select

    @override
    def add_item(self, item: Item[View]):
        if isinstance(item, BaseSelect):
            self.selects.add(item)
            def on_select(valid: bool):
                if valid:
                    self.unset.discard(item)
                    if not self.unset:
                        self.play_button.disabled = False
                else:
                    self.unset.add(item)
                    self.play_button.disabled = True
            on_select(item.has_valid_selection())
            item.on_select += on_select
        super().add_item(item)

    async def end_turn_and_die(self, interaction: Interaction):
        self.stop()
        await self.game.end_turn()
        await interaction.response.defer()
        await interaction.delete_original_response()
