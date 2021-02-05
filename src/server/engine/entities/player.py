from typing import Dict

from tornado.iostream import IOStream

from .entity import Entity
from server_utils import State, Controls


class Player(Entity):
    def __init__(self, player_id, game_state, stream: IOStream):
        self.speed = 2
        self.id = player_id
        self.x = 50  # Todo: start players in different positions when a lobby / game state is started
        self.y = 70
        self.width = 30  # todo these are guesses, figure out for real
        self.height = 50  # todo these are guesses, figure out for real
        self.game_state = game_state
        self.stream = stream  # Todo: remove this logic from the player entity class

        # Update variables
        self.change_x = 0
        self.change_y = 0

    def to_dict(self):
        return {
            State.X: self.x,
            State.Y: self.y
        }

    def new_input(self, new_input: Dict[Controls, int]):
        self.change_x = 0
        self.change_y = 0
        # Happens async whenever new input is received from client
        if new_input[Controls.MOVE_UP] and not new_input[Controls.MOVE_DOWN]:
            self.change_y = self.speed
        elif new_input[Controls.MOVE_DOWN] and not new_input[Controls.MOVE_UP]:
            self.change_y = -self.speed
        if new_input[Controls.MOVE_LEFT] and not new_input[Controls.MOVE_RIGHT]:
            self.change_x = -self.speed
        elif new_input[Controls.MOVE_RIGHT] and not new_input[Controls.MOVE_LEFT]:
            self.change_x = self.speed

    def update(self):
        # Happens when server is generating new game state to send to all clients
        self.x += self.change_x
        self.y += self.change_y

        # Check for out-of-bounds
        stage_width = self.game_state.game_stage.width
        stage_height = self.game_state.game_stage.height
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > stage_width - 1:
            self.x = stage_height - 1 - self.width

        if self.y < 0:
            self.y = 0  # todo confirm that y=0 is at bottom instead of top
        elif self.y + self.height > stage_width - 1:
            self.y = stage_height - 1 - self.height

    async def send_update(self, serialized_state):
        # Todo: remove this logic from the player entity class
        await self.stream.write(bytes(serialized_state, encoding='utf-8') + b';')
