from dataclasses import dataclass, field, asdict
from typing import Dict

from keybindings import Controls
from keyboard_controller import KEY_MAP
from mouse_controller import BUTTON_MAP


@dataclass
class InputData:
    mouse: Dict[Controls, bool] = field(
        default_factory=lambda: {k: False for k in BUTTON_MAP}
    )

    keys: Dict[Controls, bool] = field(
        default_factory=lambda: {k: False for k in KEY_MAP}
    )

    def asdict(self):
        return asdict(self)


class InputUpdate:
    latest: InputData = None    # Thread safe (i.e. atomic) reads from IO thread, updated by game thread

    @classmethod
    def put(cls, data: InputData):
        cls.latest = data

    @classmethod
    def get(cls) -> InputData:
        return cls.latest
