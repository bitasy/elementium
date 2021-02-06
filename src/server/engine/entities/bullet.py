import math

from server_utils import State, Controls
from .entity import Entity


class Bullet(Entity):
    def __init__(self, bullet_id, owner, new_input):
        self.id = bullet_id
        self.owner = owner
        self.game_state = owner.game_state
        self.x = owner.x
        self.y = owner.y
        self.speed = 5
        self.change_x = None
        self.change_y = None
        self.stage = self.game_state.game_stage

        dest_x = new_input[Controls.MOUSE_X]
        dest_y = new_input[Controls.MOUSE_Y]
        x_diff = dest_x - self.x
        y_diff = dest_y - self.y
        self.angle = math.atan2(y_diff, x_diff)
        self.change_x = math.cos(self.angle) * self.speed
        self.change_y = math.sin(self.angle) * self.speed

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < 0 or self.x > self.stage.width or self.y < 0 or self.y > self.stage.height:
            self.game_state.bullets.remove(self)

    def to_dict(self):
        return {
            State.ID: self.id,
            State.X: self.x,
            State.Y: self.y,
            State.ANGLE: self.angle,
            State.OWNER: self.owner.id
        }
