import arcade

from update_data import ServerUpdate


class Player(arcade.Sprite):

    SPRITE_SCALING = 0.5
    MOVEMENT_SPEED = 2

    def __init__(self, player_id, texture, scaling, screen_width, screen_height):
        super().__init__(texture, scaling)
        self.id = player_id
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        pass  # Todo: Interpolation & Lag Compensation

    @classmethod
    def update_all(cls, game, delta_time, keyboard_controller, update):
        sprite = game.player
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

        if update:
            player_states = update.player_states_new.copy()
            players = game.player_list
            for player in players:
                if player.id in player_states:
                    data = player_states[player.id]
                    player.center_x = data.x
                    player.center_y = data.y
                    del player_states[player.id]
                else:
                    player.remove_from_sprite_lists()

            for new_player_id, new_player in player_states.items():
                player = Player(
                    new_player_id,
                    ":resources:images/animated_characters/female_person/femalePerson_idle.png",
                    Player.SPRITE_SCALING,
                    game.window.width,
                    game.window.height
                )
                player.center_x = new_player.x
                player.center_y = new_player.y
                players.append(player)

            game.player_list.update()
