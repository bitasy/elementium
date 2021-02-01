import threading
from collections import deque

import arcade
from pymunk import Vec2d
from tornado.ioloop import IOLoop

from tornado.queues import LifoQueue

from input_data import InputData
from update_data import UpdateData

MOVE_MAP = {
    arcade.key.W: Vec2d(0, 1),
    arcade.key.S: Vec2d(0, -1),
    arcade.key.A: Vec2d(-1, 0),
    arcade.key.D: Vec2d(1, 0),
}


def apply_movement(speed, dt, current_position: Vec2d, kp) -> Vec2d:
    delta_position = sum(kp.keys[k] * MOVE_MAP[k] for k in kp.keys)
    return current_position + delta_position * speed * dt


def apply_movement_norm(speed, dt, current_position: Vec2d, kp) -> Vec2d:
    delta_position = sum(kp.keys[k] * MOVE_MAP[k] for k in kp.keys)
    return current_position + delta_position.normalized() * speed * dt


class HistoricalQueue:
    def __init__(self):
        self.queue = LifoQueue(0)  # Stack
        self.history = deque()
        self.game_thread_id = None
        self.io_thread_id = None
        self.io_loop = None

    def setup(self, game_thread_id: int, io_thread_id: int, io_loop: IOLoop):
        self.game_thread_id = game_thread_id
        self.io_thread_id = io_thread_id
        self.io_loop = io_loop

    def put(self, item):
        if threading.get_ident() == self.game_thread_id:
            self.io_loop.add_callback(lambda: self.queue.put(item))
        else:
            self.queue.put(item)

    def get(self):
        assert threading.get_ident() == self.io_thread_id
        item = self.queue.get()  # Called from IO thread
        self.history.append(item)
        self.queue.task_done()


class InputUpdate:
    latest: InputData = None    # Thread safe (i.e. atomic) reads from IO thread, updated by game thread

    @classmethod
    def put(cls, data: InputData):
        cls.latest = data

    @classmethod
    def get(cls) -> InputData:
        return cls.latest


class ServerUpdate:
    latest: UpdateData = None  # Thread safe (i.e. atomic) reads from game thread, updated by IO thread

    @classmethod
    def put(cls, data: UpdateData):  # contains previous 2 server updates for interpolation
        cls.latest = data

    @classmethod
    def get(cls) -> UpdateData:
        return cls.latest


class IOThreadFailed:
    latest: bool = False  # Did IO thread crash?

    @classmethod
    def put(cls, data: bool):
        cls.latest = data

    @classmethod
    def get(cls) -> bool:
        return cls.latest
