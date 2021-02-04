from dataclasses import dataclass


@dataclass
class PlayerData:
    updated: float = 0  # Todo use for lag compensation? Don't remember why I included this
    x: float = 0
    y: float = 0
    health: float = 0  # Todo implement
