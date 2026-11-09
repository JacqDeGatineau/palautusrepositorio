from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa."""
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: player.goals
        )

        return sorted_players[:how_many]

    def top_scorers_by_nationality(self, nationality):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        def has_nation(player):
            return player.nationality == nationality

        players = filter(has_nation,  self._players)

        sorted_players = sorted(
            list(players),
            reverse=True,
            key=sort_by_points
        )

        return sorted_players

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        team_players = filter(
            lambda player: player.team == team,
            self._players
        )

        return sorted(
            team_players,
            reverse=True,
            key=lambda player: player.points
        )
