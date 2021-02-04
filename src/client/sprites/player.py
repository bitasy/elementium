import arcade


class Player(arcade.Sprite):

    MOVEMENT_SPEED = 2

    def __init__(self, texture, scaling, screen_width, screen_height):
        super().__init__(texture, scaling)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        pass  # Todo: Interpolation & Lag Compensation
