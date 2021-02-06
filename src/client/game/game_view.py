import arcade

from ..data.dataclasses.input_data import InputData, InputUpdate
from .keyboard_controller import KeyboardController
from .mouse_controller import MouseController
from .frame_updater import on_update
from .game_renderer import on_draw
from .setup_stage import setup_stage
from ..data.client_utils import IOThreadFailed


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.mouse_controller = MouseController()
        self.keyboard_controller = KeyboardController()
        setup_stage(self)

    def on_draw(self):
        on_draw(self)

    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_controller.on_mouse_press(self, x, y, button)

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_controller.on_mouse_release(x, y, button)

    def on_key_press(self, key, modifiers):
        self.keyboard_controller.on_key_press(key)

    def on_key_release(self, key, modifiers):
        self.keyboard_controller.on_key_release(key)

    def on_update(self, delta_time):
        if IOThreadFailed.get():
            raise IOError("do something about crashed IO thread")
        keyboard_state = self.keyboard_controller.get_state()
        mouse_state = self.mouse_controller.get_state()
        input_state = InputData(keyboard_state, mouse_state)
        InputUpdate.put(input_state)
        on_update(self, delta_time, self.keyboard_controller)
