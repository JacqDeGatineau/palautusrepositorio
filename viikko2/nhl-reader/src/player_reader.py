import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        players_file = requests.get(self._url).json()
        return [Player(player_dict) for player_dict in players_file]
