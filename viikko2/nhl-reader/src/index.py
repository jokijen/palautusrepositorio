from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():

    console = Console()
    console.print("NHL statistics by nationality", style="italic")

    console.print("\nSelect season " +
                  "[magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/magenta]: ", end="")
    season = input()
    
    while True:
        console.print("\nSelect nationality (or x to quit) " +
                      "[magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/magenta]: ")
        nationality = input()

        if nationality == "x":
            break

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)
        
        table = Table(title=f"\nTop scorers of {nationality} season {season}\n", style="italic")
        table.add_column("name", justify="left", style="cyan")
        table.add_column("team", justify="left", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for p in players:
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))
        
        console.print(table)


if __name__ == "__main__":
    main()
