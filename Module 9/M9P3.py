
# Function to calculate miles per gallon
def calculate_mpg(miles, gallons):
    if gallons == 0:  # Avoid division by zero
        return 0.0
    return miles / gallons

# Initialize trip counter
trip_count = 0

print("Trip MPG Calculator")
print("Enter 'q' for destination to quit")

# Loop for user to enter multiple trips
while True:
    print("\nEnter trip details:")
    destination = input("Enter destination city (or 'q' to quit): ")
    
    # Check if user wants to quit
    if destination.lower() == 'q':
        break
    
    # Get miles and gallons
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))
    
    # Calculate MPG using function
    mpg = calculate_mpg(miles, gallons)
    
    # Increment trip counter
    trip_count += 1
    
    # Display trip details
    print(f"\nDestination: {destination}")
    print(f"Miles Travelled: {miles:.1f}")
    print(f"Miles Per Gallon: {mpg:.1f}")

# Display trip count
print(f"\nTotal number of trips entered: {trip_count}")
