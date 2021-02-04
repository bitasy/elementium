from entities.entity import Entity


class Coin(Entity):
    def __init__(self, coin_id, x, y):
        self.id = coin_id
        self.x = x
        self.y = y
