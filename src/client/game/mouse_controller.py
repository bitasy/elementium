from .keybindings import Controls, bindings

SPRITE_SCALING_LASER = 0.8
BULLET_SPEED = 5

BUTTON_MAP = {
    Controls.MOUSE_LEFT: False,
    Controls.MOUSE_RIGHT: False,
    Controls.MOUSE_X: 0,
    Controls.MOUSE_Y: 0,
}


class MouseController:
    def __init__(self):
        self.state = BUTTON_MAP.copy()


    def on_mouse_press(self, game, x, y, button):
        if button in bindings:
            self.state[bindings[button]] = True
        self.state[Controls.MOUSE_X] = x
        self.state[Controls.MOUSE_Y] = y
        """
        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        # Position the bullet at the player's current location
        start_x = game.player_sprite.center_x
        start_y = game.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in game.view_bottom and game.view_left.
        dest_x = x
        dest_y = y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        bullet.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        game.bullet_list.append(bullet)
        """

    def on_mouse_release(self, x, y, button):
        if button in bindings:
            self.state[bindings[button]] = False
        self.state[Controls.MOUSE_X] = x
        self.state[Controls.MOUSE_Y] = y

    def get_state(self):
        return self.state
