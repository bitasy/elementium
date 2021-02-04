import json
from dataclasses import dataclass
from typing import Dict

from client_utils import State
from player_data import PlayerData


@dataclass
class UpdateData:
    player_states_old: Dict[int, PlayerData]  # todo use for lag compensation
    player_states_new: Dict[int, PlayerData]

    @staticmethod
    def from_json(data):
        old = ServerUpdate.get().player_states_new.copy()
        new = {}
        d = json.loads(data)
        for player_id, player_data in d[str(State.PLAYERS.value)].items():
            new[player_id] = PlayerData(
                x=player_data[str(State.X.value)],
                y=player_data[str(State.Y.value)]
            )
        return UpdateData(old, new)


class ServerUpdate:
    latest: UpdateData = None  # Thread safe (i.e. atomic) reads from game thread, updated by IO thread

    @classmethod
    def put(cls, data: UpdateData):  # contains previous 2 server updates for interpolation
        cls.latest = data

    @classmethod
    def get(cls) -> UpdateData:
        return cls.latest
