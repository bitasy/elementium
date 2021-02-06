import math

import arcade

from bullet import Bullet
from player import Player
from update_data import ServerUpdate


def on_update(game, delta_time, keyboard_controller):
    update = ServerUpdate.get()
    Player.update_all(game, delta_time, keyboard_controller, update)
    Bullet.update_all(game, delta_time, update)
