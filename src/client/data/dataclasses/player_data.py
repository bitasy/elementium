from dataclasses import dataclass


@dataclass
class PlayerData:
    updated: float = 0
    x: float = 0
    y: float = 0
    health: float = 0
