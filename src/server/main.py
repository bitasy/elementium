import sys

from tornado.ioloop import IOLoop

from engine.game_state import GameState
from web.webserver import GameServer

TICK_RATE = 32

if __name__ == '__main__':
    lobby_map = {}
    # Temporary global lobby
    global_lobby = GameState()
    lobby_map[1] = global_lobby
    server = GameServer(lobby_map)
    server.listen(int(sys.argv[1]))
    IOLoop.current().run_sync(lambda: global_lobby.start(TICK_RATE))
    IOLoop.current().start()
