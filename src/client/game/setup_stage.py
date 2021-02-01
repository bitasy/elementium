import random

import arcade

from keyboard_controller import KeyboardController
from player import Player

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50


def setup_stage(game):
    game.score = 0

    # Load sounds. Sounds from kenney.nl
    game.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
    game.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

    arcade.set_background_color(arcade.color.AMAZON)

    """ Set up the game and initialize the variables. """

    # Sprite lists
    game.player_list = arcade.SpriteList()
    game.coin_list = arcade.SpriteList()
    game.bullet_list = arcade.SpriteList()

    # Set up the player
    game.score = 0

    # Image from kenney.nl
    game.player_sprite = Player(
        ":resources:images/animated_characters/female_person/femalePerson_idle.png",
        SPRITE_SCALING_PLAYER,
        game.window.width,
        game.window.height
    )
    game.player_sprite.center_x = 50
    game.player_sprite.center_y = 70
    game.player_list.append(game.player_sprite)

    # Create the coins
    for i in range(COIN_COUNT):
        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(game.window.width)
        coin.center_y = random.randrange(120, game.window.height)

        # Add the coin to the lists
        game.coin_list.append(coin)

    # Set the background color
    arcade.set_background_color(arcade.color.AMAZON)