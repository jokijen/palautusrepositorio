from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Not, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print("******* Fewer than:")

    matcher2 = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
    )

    for player in stats.matches(matcher2):
        print(player)

    print("******* All:")

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("******* Not:")

    matcher3 = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )
    for player in stats.matches(matcher3):
        print(player)


if __name__ == "__main__":
    main()
