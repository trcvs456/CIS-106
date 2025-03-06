# Get user input for start, stop, and increment values
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment value: "))

# Ensure the increment is valid to prevent infinite loops
if increment == 0:
    print("Increment value cannot be zero.")
else:
    # Use a while loop to display numbers from start to stop using the increment
    while start <= stop:
        print(start)
        start += increment  # Increase start by the increment value
