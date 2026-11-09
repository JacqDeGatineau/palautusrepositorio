from player_reader import PlayerReader

class PlayerStats: 
    def __init__(self, reader):
        self._players = reader.get_players()


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
