class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self._score1 = 0
        self._score2 = 0
        self.tilanteet= ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self._score1 += 1
        elif player_name == self.player2_name:
            self._score2 += 1

    def get_score(self):
        if self._score1 == self._score2:
            return self.tasapeli()

        elif self._score1 >= 4 or self._score2 >= 4:
            return self.etu()

        return self.peli()


    def tasapeli(self):
        if self._score1 < 4:
            return f"{self.tilanteet[self._score1]}-All"
        else:
            return "Deuce"

    def etu(self):
        minus_result = self._score1 - self._score2
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def peli(self):
        return f"{self.tilanteet[self._score1]}-{self.tilanteet[self._score2]}"



