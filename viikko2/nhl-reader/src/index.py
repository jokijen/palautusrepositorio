import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.is_finnish:
            players.append(player)

    sorted_players = sorted(players, key=lambda plr: plr.points, reverse=True)
    print("Players from FIN\n")

    for player in sorted_players:
        print(player)


if __name__ == "__main__":
    main()
