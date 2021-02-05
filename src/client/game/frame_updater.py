import arcade

from player import Player
from update_data import ServerUpdate


def on_update(game, delta_time, keyboard_controller):
    sprite = game.player_sprite
    speed = sprite.MOVEMENT_SPEED

    sprite.change_x = 0
    sprite.change_y = 0

    if keyboard_controller.up_pressed() and not keyboard_controller.down_pressed():
        sprite.change_y = speed
    elif keyboard_controller.down_pressed() and not keyboard_controller.up_pressed():
        sprite.change_y = -speed
    if keyboard_controller.left_pressed() and not keyboard_controller.right_pressed():
        sprite.change_x = -speed
    elif keyboard_controller.right_pressed() and not keyboard_controller.left_pressed():
        sprite.change_x = speed

    print('x ' + str(sprite.change_x))
    print('y ' + str(sprite.change_y))

    update = ServerUpdate.get()
    states = update.player_states_new.copy()
    players = game.player_list
    for player in players:
        if player.id in states:
            data = states[player.id]
            player.center_x = data.x
            player.center_y = data.y
            del states[player.id]
        else:
            player.remove_from_sprite_lists()

    for new_player_id, new_player in states.items():
        players.append(Player(
            new_player_id,
            ":resources:images/animated_characters/female_person/femalePerson_idle.png",
            Player.SPRITE_SCALING,
            game.window.width,
            game.window.height
        ))

    game.player_list.update()

    # Call update on all sprites
    game.bullet_list.update()

    # Loop through each bullet
    for bullet in game.bullet_list:

        # Check this bullet to see if it hit a coin
        hit_list = arcade.check_for_collision_with_list(bullet, game.coin_list)

        # If it did, get rid of the bullet
        if len(hit_list) > 0:
            bullet.remove_from_sprite_lists()

        # For every coin we hit, add to the score and remove the coin
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            game.score += 1

        # If the bullet flies off-screen, remove it.
        if bullet.bottom > game.window.width or bullet.top < 0 or bullet.right < 0 or bullet.left > game.window.width:
            bullet.remove_from_sprite_lists()
