# Function to load data from file
def load_player_data(filename):
    player_names = []
    batting_averages = []
    with open(filename, 'r') as file:
        for line in file:
            name, average = line.strip().split()
            player_names.append(name)
            batting_averages.append(float(average))
    return player_names, batting_averages

# Function to display all player names and averages
def display_players(names, averages):
    print("Player List and Batting Averages:")
    for i in range(len(names)):
        print(f"{names[i]} - Batting Average: {averages[i]:.3f}")

# Function to search for a player and display batting average
def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"{names[i]} - Batting Average: {averages[i]:.3f}")
            found = True
            break
    if not found:
        print(f"{search_name} not found in the player list.")

# Main program
filename = "players.txt"
player_names, batting_averages = load_player_data(filename)

display_players(player_names, batting_averages)
print()

# Repeatedly ask user to search for a player
while True:
    search_name = input("Enter a last name to search (or type 'exit' to quit): ")
    if search_name.lower() == 'exit':
        print("Exiting the search.")
        break
    search_player(player_names, batting_averages, search_name)
    print()
