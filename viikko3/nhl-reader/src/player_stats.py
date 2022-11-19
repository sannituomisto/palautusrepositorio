def sort_by_points(player):
    return player.goals + player.assists

class PlayerStats:
    def __init__(self, reader):
        self._players=reader.get_players()
        self._players_by_nationality=[]


    def top_scorers_by_nationality(self,nationality):
        for player in self._players:
            if player.nationality == nationality:
                self._players_by_nationality.append(player)
                
                
        sorted_players = sorted(
            self._players_by_nationality,
            reverse=True,
            key=sort_by_points)
        
        return sorted_players