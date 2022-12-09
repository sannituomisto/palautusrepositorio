from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(5, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(1, "goals")),
    #     PlaysIn("NYR")
    # )

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )


    for player in stats.matches(matcher):
        print(player)

    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))




if __name__ == "__main__":
    main()