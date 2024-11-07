import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

"""
        nationality = "FIN"

        for player_dict in response:
            player = Player(player_dict)
            if player.is_nationality(nationality):
                players.append(player)

        sorted_players = sorted(players, key=lambda plr: plr.points, reverse=True)
        print("Players from FIN\n")

        for player in sorted_players:
            print(player)
"""
