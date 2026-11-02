import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
                PlayerReaderStub()
        )

    def test_search(self):
        name = "Semenko"
        self.assertEqual(self.stats.search(name).name, "Semenko")

    def test_search_fail(self):
        self.assertEqual(self.stats.search("Koivu"), None)

    def test_team(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    def test_top_points(self):
        points = self.stats.top(3, SortBy.POINTS)
        names = []
        for name in points:
            names.append(name.name)

        tops = ["Gretzky", "Lemieux", "Yzerman", "Kurri"];
        self.assertEqual(names, tops);

    def test_top_goals(self):
        goals = self.stats.top(2, SortBy.GOALS)
        names = []
        for name in goals:
            names.append(name.name)

        goal_points = ["Lemieux", "Yzerman", "Kurri"];
        self.assertEqual(names, goal_points);

    def test_top_assists(self):
        assists = self.stats.top(2, SortBy.ASSISTS)
        names = []
        for name in assists:
            names.append(name.name)

        assist_points = ["Gretzky", "Yzerman", "Lemieux"];
        self.assertEqual(names, assist_points);

    def test_top_input(self):
        none = self.stats.top(2, "nonce")

        self.assertEqual(None, none)
