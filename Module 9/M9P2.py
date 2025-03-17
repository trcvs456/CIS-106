# Function to calculate batting average
def calculate_batting_average(hits, at_bats):
    if at_bats == 0:  # Avoid division by zero
        return 0.0
    return hits / at_bats

# Initialize player counter
player_count = 0

print("Baseball Batting Average Calculator")
print("Enter 'q' for last name to quit")

# Loop for user to enter multiple players
while True:
    print("\nEnter player details:")
    last_name = input("Enter player's last name (or 'q' to quit): ")
    
    # Check if user wants to quit
    if last_name.lower() == 'q':
        break
    
    # Get hits and at bats
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))
    
    # Calculate batting average using function
    batting_average = calculate_batting_average(hits, at_bats)
    
    # Increment player counter
    player_count += 1
    
    # Display player details
    print(f"\nPlayer: {last_name}")
    print(f"Batting Average: {batting_average:.3f}")

# Display player count
print(f"\nTotal number of players entered: {player_count}")
