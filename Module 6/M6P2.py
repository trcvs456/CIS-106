# Function to determine unit cost based on part number
def get_unit_cost(part_num):
    if part_num in ["10", "55"]:
        return 1.00
    elif part_num == "99":
        return 2.00
    elif part_num in ["80", "70"]:
        return 3.00
    else:
        return 5.00

# Get user input
part_num = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

# Determine unit cost
unit_cost = get_unit_cost(part_num)

# Calculate total cost
total_cost = quantity * unit_cost

# Display results
print("Part Number:", part_num)
print("Unit Cost: ${:.2f}".format(unit_cost))
print("Total Cost: ${:.2f}".format(total_cost))

