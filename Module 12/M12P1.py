# Assign 10 last names to an array (list)
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Function to display names in original order
def display_names(names):
    print("Names in original order:")
    for name in names:
        print(name)

# Function to display names in reverse order
def display_names_reverse(names):
    print("Names in reverse order:")
    for name in reversed(names):
        print(name)

# Call the functions
display_names(last_names)
print()  # Blank line for spacing
display_names_reverse(last_names)
