import math

import arcade


class Bullet(arcade.Sprite):

    SPRITE_SCALING = 0.8
    MOVEMENT_SPEED = 5

    def __init__(self, bullet_id, texture, scaling, screen_width, screen_height):
        super().__init__(texture, scaling)
        self.id = bullet_id
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        pass  # Todo: Interpolation & Lag Compensation

    @classmethod
    def update_all(cls, game, delta_time, update):
        bullet_states = update.bullet_states.copy()
        bullets = game.bullet_list
        for bullet in bullets:
            if bullet.id in bullet_states:
                data = bullet_states[bullet.id]
                bullet.center_x = data.x
                bullet.center_y = data.y
                del bullet_states[bullet.id]
            else:
                bullet.remove_from_sprite_lists()

        for new_bullet_id, new_bullet in bullet_states.items():
            is_player = new_bullet.owner == game.player.id
            color = "Blue" if is_player else "Red"
            bullet = Bullet(
                new_bullet_id,
                ":resources:images/space_shooter/laser%s01.png" % color,
                Bullet.SPRITE_SCALING,
                game.window.width,
                game.window.height
            )
            bullet.center_x = new_bullet.x
            bullet.center_y = new_bullet.y
            bullet.angle = math.degrees(new_bullet.angle) - (0 if is_player else 90)
            bullets.append(bullet)
        game.bullet_list.update()
