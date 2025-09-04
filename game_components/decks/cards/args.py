from core.cards import ArgFunc, Argument, CardColor, Option
from game import Game


@ArgFunc.create
def choose_player(game: Game, placeholder: str = 'Choose a player.', * , skip_self: bool = False):
    return Argument(
        placeholder=placeholder,
        options=tuple(
            Option(
                name=player.display_name,
                id=str(player.id),
                value=player
            )
            for player in game.table.starting_with_you
            if not (skip_self and player == game.active_player)
        )
    )

@ArgFunc.create
def choose_color(game: Game, placeholder: str = 'Choose a color.', ):
    return Argument(
        placeholder=placeholder,
        options=tuple(
            Option(
                name=(color.name or '???').title(),
                id=str(color.value),
                value=color
            )
            for color in CardColor
        )
    )

@ArgFunc.create
def choose_card(game: Game, *, requires_playable: bool = False):
    # TODO: is there a way to prevent the same card from being selected?
    return Argument(
        placeholder='Choose a card.',
        options=tuple(
            Option(
                name=card.display_name,
                id=str(card.uuid),
                value=card
            )
            for card in game.active_player.hand.sorted()
            if game.can_play(card, game.active_pile) or not requires_playable
        )
    )
