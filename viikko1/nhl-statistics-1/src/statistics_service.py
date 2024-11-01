from player_reader import PlayerReader
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals

        def sort_by_assists(player):
            return player.assists

        if sort_by == SortBy.POINTS:
            sorting_criteria = sort_by_points
        elif sort_by == SortBy.GOALS:
            sorting_criteria = sort_by_goals
        elif sort_by == SortBy.ASSISTS:
            sorting_criteria = sort_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorting_criteria
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
