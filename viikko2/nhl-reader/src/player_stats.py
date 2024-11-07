from player_reader import PlayerReader
from player import Player


class PlayerStats:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        country_players = []

        for player in self._players:
            if player.is_nationality(nationality):
                country_players.append(player)

        top_scorers = sorted(
            country_players, 
            key=lambda plr: plr.points, 
            reverse=True
        )

        return top_scorers
