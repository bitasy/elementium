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
    ANGLE = 7
    OWNER = 8


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, max_len=None):
        self.head = None
        self.tail = None
        self.count = 0
        self.max_len = max_len

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def set_head(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.count = 1

    def get_count(self):
        return self.count

    def append(self, data):
        if self.count == 0:
            self.set_head(data)
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.count += 1
            if self.max_len is not None and self.count > self.max_len:
                self.head = self.head.next
                self.head.prev = None


def stringify(data):  # For now, unmodified json is easiest
    return json.dumps(data, separators=(',', ':'))
