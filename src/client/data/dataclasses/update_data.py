import json
from dataclasses import dataclass, asdict
from typing import List

from player_data import PlayerData


@dataclass
class UpdateData:
    player_states_old: List[PlayerData]  # Null from the server, updated here
    player_states_new: List[PlayerData]

    def to_json(self):
        d = dict(
            player_states=[asdict(p) for p in self.player_states_old],
        )
        return json.dumps(d)

    def from_json(self, data):
        self.player_states_old = self.player_states_new.copy()
        self.player_states_new = []
        d = json.loads(data)
        for i, p in enumerate(d['player_states']):
            self.player_states_new[i] = PlayerData(**p)
