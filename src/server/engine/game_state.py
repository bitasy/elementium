import time

from tornado import gen
from tornado.iostream import StreamClosedError

from .entities.bullet import Bullet
from .entities.coin import Coin
from .entities.player import Player
from .game_stage import GameStage
from server_utils import stringify, State


class GameState:
    def __init__(self):
        super().__init__()
        self.players: [Player] = []
        self.bullets: [Bullet] = []
        self.coins: [Coin] = []
        self.prev_time = 0
        self.game_stage = GameStage(1600, 900)
        self.game_tick = 0

    async def start(self, rate: int = 32):  # Match client rate
        self.prev_time = time.time()
        while True:
            timer = gen.sleep(1 / rate)
            await self.tick()
            await timer

    async def tick(self):
        try:
            for player in self.players:
                player.update()  # Based on player-stored new input
            state = self.serialize_state()
            for player in self.players:
                await player.send_update(state)
            self.game_tick += 1
            self.prev_time = time.time()  # Todo use for lag compensation or whatever else
        except StreamClosedError as e:
            print("player " + player.id + " disconnected ")
            self.players.remove(player)

    def add_player(self, player_id, stream):
        player = Player(player_id, self, stream)
        self.players.append(player)
        return player

    def serialize_state(self) -> str:
        # Todo: track bullets and coins, implement their to_dict() functions
        # Todo: instead of sending entire game state, only send changes since last ack'd state for client
        # Todo: Lag compensation (biggie)
        return stringify({
            State.PLAYERS: {player.id: player.to_dict() for player in self.players},
            State.TICK: self.game_tick
        })
