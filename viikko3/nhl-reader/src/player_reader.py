from player import Player
import requests

class PlayerReader:
    def __init__(self,url):
        self._response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    def get_players(self):
        players= []
        for player_dict in self._response:
                player = Player(
                    player_dict['name'], player_dict["nationality"], player_dict['team'], player_dict['goals'], player_dict['assists']
                )

                players.append(player)
        
        return players