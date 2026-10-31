import unittest
from statistics_service import StatisticsService
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

    def test_top(self):
        top = self.stats.top(3)[0].name

        self.assertEqual(top, "Gretzky")
