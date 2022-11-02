from player_reader import PlayerReader
from statistics import Statistics
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def main():
    io=PlayerReader()
    stats = Statistics(io)
    philadelphia_flyers_players = stats.team("PHI")

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS.value):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS.value):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS.value):
        print(player)



if __name__ == "__main__":
    main()
