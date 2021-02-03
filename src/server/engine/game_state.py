from tornado.ioloop import PeriodicCallback


class GameLoop:
    def __init__(self, player_lobby_map):
        super().__init__()
        self.player_lobby_map = player_lobby_map

    def start(self, rate: int = 32):  # Match client rate
        PeriodicCallback(self.tick, 1000 / rate).start()

        # reminder: need to lock around accessing game state to send to clients so they dont corrupt it on update

    def tick(self):

        pass
