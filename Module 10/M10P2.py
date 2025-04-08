# Function to calculate wall square footage
def calculate_wall_area(length, width, height):
    return 2 * length * height + 2 * width * height

# Bonus: Function to calculate ceiling or floor area
def calculate_ceiling_floor_area(length, width):
    return length * width

# Function to calculate gallons needed
def calculate_gallons(area, coverage_per_gallon=50):
    return area / coverage_per_gallon

# Main loop
while True:
    user_input = input("Do you want to calculate paint needed? (Yes or No): ").strip().lower()
    
    if user_input == "yes":
        try:
            # Get dimensions
            length = float(input("Enter the length of the room (in feet): "))
            width = float(input("Enter the width of the room (in feet): "))
            height = float(input("Enter the height of the room (in feet): "))

            # Calculate wall area and paint gallons
            wall_area = calculate_wall_area(length, width, height)
            wall_gallons = calculate_gallons(wall_area)

            print(f"\nWall area: {wall_area:.2f} square feet")
            print(f"Gallons of paint needed for walls: {wall_gallons:.2f}")

            # Bonus: Calculate ceiling/floor area and gallons
            ceiling_area = calculate_ceiling_floor_area(length, width)
            ceiling_gallons = calculate_gallons(ceiling_area)

            print(f"\nCeiling/Floor area: {ceiling_area:.2f} square feet")
            print(f"Gallons of paint or varnish needed for ceiling/floor: {ceiling_gallons:.2f}")
            print("-" * 40)

        except ValueError:
            print("Invalid input. Please enter numeric values for dimensions.")
    elif user_input == "no":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")

