import os
import sys
import threading
import arcade
import random
from .game.game_view import GameView
from .data.webclient import WebClient

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Elementium (In Dev)"

TICK_RATE = 32


def game():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        sys.argv.append("13.57.249.171")
        sys.argv.append("8889")
        sys.argv.append(str(random.randint(0, 10000)))
        os.chdir(sys._MEIPASS)
    net = WebClient(TICK_RATE)
    client_thread = threading.Thread(target=net.start_client, daemon=True)
    client_thread.start()
    game()
