from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def show_table(players, season, nationality):
    table = Table(title=f"Players from {nationality}, season {season}")
    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold yellow")

    for p in players:
        table.add_row(
            p.name,
            p.team,
            str(p.goals),
            str(p.assists),
            str(p.points),
        )

    Console().print(table)

def main():
    season = input("Season [2024-25]: ") or "2024-25"
    nationality = (input("Nationality [FIN]: ") or "FIN").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    players = stats.top_scorers_by_nationality(nationality)

    show_table(players, season, nationality)

if __name__ == "__main__":
    main()
