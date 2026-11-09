import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "team": "AAA",
                "goals": 10,
                "assists": 20
            }),
            Player({
                "name": "Player Two",
                "nationality": "SWE",
                "team": "AAA",
                "goals": 15,
                "assists": 5
            }),
            Player({
                "name": "Player Three",
                "nationality": "FIN",
                "team": "BBB",
                "goals": 5,
                "assists": 24
            })
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_goal_scorers_returns_requested_number_in_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            ["Player Two", "Player One"],
            [player.name for player in players]
        )

    def test_top_scorers_by_nationality_returns_players_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            ["Player One", "Player Three"],
            [player.name for player in players]
        )

    def test_top_scorers_by_team_returns_only_team_players_by_points(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(
            ["Player One", "Player Two"],
            [player.name for player in players]
        )


if __name__ == "__main__":
    unittest.main()
