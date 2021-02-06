from dataclasses import dataclass


@dataclass
class BulletData:
    updated: float = 0
    x: float = 0
    y: float = 0
    angle: float = 0
    owner: str = None
