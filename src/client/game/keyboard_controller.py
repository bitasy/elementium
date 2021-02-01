from keybindings import Controls, bindings

KEY_MAP = {
    Controls.MOVE_UP: False,
    Controls.MOVE_DOWN: False,
    Controls.MOVE_LEFT: False,
    Controls.MOVE_RIGHT: False,
}


class KeyboardController:
    def __init__(self):
        self.state = KEY_MAP.copy()

    def on_key_press(self, key):
        if key in bindings:
            self.state[bindings[key]] = True

    def on_key_release(self, key):
        if key in bindings:
            self.state[bindings[key]] = False

    def get_state(self):
        return self.state

    def up_pressed(self):
        return self.state[Controls.MOVE_UP]

    def down_pressed(self):
        return self.state[Controls.MOVE_DOWN]

    def left_pressed(self):
        return self.state[Controls.MOVE_LEFT]

    def right_pressed(self):
        return self.state[Controls.MOVE_RIGHT]
