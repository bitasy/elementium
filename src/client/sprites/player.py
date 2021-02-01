import arcade


class Player(arcade.Sprite):

    MOVEMENT_SPEED = 2

    def __init__(self, texture, scaling, screen_width, screen_height):
        super().__init__(texture, scaling)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0

        elif self.right > self.screen_width - 1:
            self.right = self.screen_height - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > self.screen_width - 1:
            self.top = self.screen_height - 1
