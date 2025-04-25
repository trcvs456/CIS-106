# Function to load players from a file into a dictionary (from Problem 3)
def load_players(file_name):
    players_dict = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, average = line.strip().split()
                players_dict[name] = float(average)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return players_dict

# Function to look up a player's batting average
def lookup_player(players_dict):
    while True:
        name = input("\nEnter a player’s last name to look up (or type 'exit' to stop): ").strip()
        if name.lower() == 'exit':
            print("Exiting lookup.")
            break
        elif name in players_dict:
            print(f"{name}'s batting average is: {players_dict[name]:.3f}")
        else:
            print(f"No player named {name} was found. Please try again.")

# Load players from the file used in Problem 3
players = load_players('players.txt')

# Print the list to confirm (from Problem 3 reused here)
print(f"\n{'Player Name':<15}{'Batting Average'}")
for name, avg in players.items():
    print(f"{name:<15}{avg:.3f}")

# Start player lookup (new functionality)
lookup_player(players)
