import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        player_name = "Semenko"
        player = self.stats.search(player_name)
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_not_existing_player(self):
        player_name = "Litmanen"
        player = self.stats.search(player_name)
        self.assertIsNone(player)

    def test_return_team_players(self):
        team_name = "EDM"
        returned_players = self.stats.team(team_name)
        returned_players_list = [(p.name, p.team, p.goals, p.assists) for p in returned_players]

        correct_players = [
            ("Semenko", "EDM", 4, 12),
            ("Kurri",   "EDM", 37, 53),
            ("Gretzky", "EDM", 35, 89)
        ]

        self.assertListEqual(returned_players_list, correct_players)

    def test_get_top_two_players_on_points(self):
        top_players = self.stats.top(2)
        top_players_list = [(p.name, p.team, p.goals, p.assists) for p in top_players]

        correct_two = [
            ("Gretzky", "EDM", 35, 89),
            ("Lemieux", "PIT", 45, 54)
        ]

        self.assertListEqual(top_players_list, correct_two)

    def test_get_top_three_players_on_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        top_players_list = [(p.name, p.team, p.goals, p.assists) for p in top_players]

        correct_three = [
            ("Lemieux", "PIT", 45, 54),
            ("Yzerman", "DET", 42, 56),
            ("Kurri",   "EDM", 37, 53)
        ]

        self.assertListEqual(top_players_list, correct_three)

    def test_get_top_four_players_on_assists(self):
        top_players = self.stats.top(4, SortBy.ASSISTS)
        top_players_list = [(p.name, p.team, p.goals, p.assists) for p in top_players]

        correct_four = [
            ("Gretzky", "EDM", 35, 89),
            ("Yzerman", "DET", 42, 56),
            ("Lemieux", "PIT", 45, 54),
            ("Kurri",   "EDM", 37, 53)
        ]

        self.assertListEqual(top_players_list, correct_four)
