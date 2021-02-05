import threading
import arcade
from game_view import GameView
from webclient import WebClient

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Elementium (In Dev)"


def game():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    net = WebClient()
    client_thread = threading.Thread(target=net.start_client)
    client_thread.start()
    game()
