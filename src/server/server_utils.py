# Control keys
import json
from enum import Enum


class Controls(int, Enum):
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


class State(int, Enum):
    ID = 0
    X = 1
    Y = 2
    TICK = 3
    PLAYERS = 4
    BULLETS = 5
    COINS = 6


def stringify(data):  # For now, unmodified json is easiest
    return json.dumps(data, separators=(',', ':'))
