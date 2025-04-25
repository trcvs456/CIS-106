# Function to load players from a file into a dictionary
def load_players(file_name):
    players_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            name, average = line.split()
            players_dict[name] = float(average)
    return players_dict

# Load the players from file
players = load_players('players.txt')

# Print the dictionary contents in two columns
print(f"{'Player Name':<15}{'Batting Average'}")
for name, avg in players.items():
    print(f"{name:<15}{avg:.3f}")
