import arcade


def on_draw(game):
    """ Render the screen. """

    # This command has to happen before we start drawing
    arcade.start_render()

    # Draw all the sprites.
    game.coin_list.draw()
    game.player_list.draw()
    game.bullet_list.draw()

    for player in game.player_list:
        arcade.draw_text(
            player.id,
            player.center_x,
            player.top,
            arcade.color.WHITE,
            14,
            align="center",
            anchor_x="center",
            anchor_y="bottom"
        )
