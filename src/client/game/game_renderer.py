import arcade


def on_draw(game):
    """ Render the screen. """

    # This command has to happen before we start drawing
    arcade.start_render()

    # Draw all the sprites.
    game.coin_list.draw()
    game.player_list.draw()
    game.bullet_list.draw()

    # Put the text on the screen.
    #output = f"Score: {game.score}"
    #arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
