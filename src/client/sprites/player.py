import arcade


class Player(arcade.Sprite):

    SPRITE_SCALING = 0.5
    MOVEMENT_SPEED = 2

    def __init__(self, player_id, texture, scaling, screen_width, screen_height):
        super().__init__(texture, scaling)
        self.id = player_id
        self.screen_width = screen_width
        self.screen_height = screen_height
        print(self.top)
        print(self.bottom)
        print(self.left)
        print(self.right)

    def update(self):
        pass  # Todo: Interpolation & Lag Compensation
