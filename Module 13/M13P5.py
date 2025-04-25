# Function to calculate paint required for a room
def calculate_paint(length, width, height):
    area = 2 * (length * height + width * height)  # Area for walls only (no ceiling)
    return math.ceil(area / 50)  # One gallon per 50 square feet

# Function to get room details and calculate paint required
def room_paint_calculator():
    rooms_paint = {}
    while True:
        room_name = input("Enter room name (or 'done' to finish): ")
        if room_name.lower() == 'done':
            break
        length = float(input(f"Enter the length of {room_name}: "))
        width = float(input(f"Enter the width of {room_name}: "))
        height = float(input(f"Enter the height of {room_name}: "))
        
        # Calculate gallons needed for the room
        gallons = calculate_paint(length, width, height)
        rooms_paint[room_name] = gallons
    
    # Print the dictionary content (room name and paint required)
    print("\nRoom Paint Requirements:")
    for room, gallons in rooms_paint.items():
        print(f"{room:<15}{gallons} gallons")

# Call the room paint calculator function
room_paint_calculator()
 
