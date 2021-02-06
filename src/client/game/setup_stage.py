import random
import sys

import arcade

from ..sprites.player import Player

SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50


def setup_stage(game):
    game.score = 0

    arcade.set_background_color(arcade.color.AMAZON)

    """ Set up the game and initialize the variables. """

    # Sprite lists
    game.player_list = arcade.SpriteList()
    game.coin_list = arcade.SpriteList()
    game.bullet_list = arcade.SpriteList()

    # Set up the player
    game.score = 0

    # Image from kenney.nl
    game.player = Player(
        sys.argv[3],
        "resources/imgs/femaleAdventurer_idle.png",
        Player.SPRITE_SCALING,
        game.window.width,
        game.window.height
    )
    game.player.center_x = 50
    game.player.center_y = 70
    game.player_list.append(game.player)

    # Create the coins
    for i in range(COIN_COUNT):
        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite("resources/imgs/bush.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(game.window.width)
        coin.center_y = random.randrange(10, game.window.height)

        # Add the coin to the lists
        game.coin_list.append(coin)

    # Set the background color
    arcade.set_background_color(arcade.color.AMAZON)
