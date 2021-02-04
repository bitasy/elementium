from entities.entity import Entity
from player import Player


class Bullet(Entity):
    def __init__(self, bullet_id, owner: Player, x, y):
        self.id = bullet_id
        self.owner_id = owner.id
        self.x = x
        self.y = y
