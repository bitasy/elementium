from enum import Enum

import arcade


class Controls(Enum):
    # Mouse
    MOUSE_LEFT = 0
    MOUSE_RIGHT = 1
    MOUSE_X = 2
    MOUSE_Y = 3
    SCROLL_ANGLE = 4

    # Keyboard
    MOVE_UP = 5
    MOVE_DOWN = 6
    MOVE_LEFT = 7
    MOVE_RIGHT = 8


bindings = {
    arcade.MOUSE_BUTTON_LEFT: Controls.MOUSE_LEFT,
    arcade.MOUSE_BUTTON_RIGHT: Controls.MOUSE_RIGHT,
    arcade.key.W: Controls.MOVE_UP,
    arcade.key.S: Controls.MOVE_DOWN,
    arcade.key.A: Controls.MOVE_LEFT,
    arcade.key.D: Controls.MOVE_RIGHT
}
