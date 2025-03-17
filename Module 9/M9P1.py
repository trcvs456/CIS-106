# Function to calculate total with possible discount
def calculate_total(quantity, price):
    total = quantity * price
    # Apply 10% discount if total exceeds $10,000
    if total > 10000.00:
        total = total * 0.9  # 10% discount
    return total

# Initialize sum of all totals
grand_total = 0.0

# Loop for user to enter multiple items
while True:
    print("\nEnter item details (or 'q' to quit):")
    user_input = input("Enter quantity (or 'q' to quit): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'q':
        break
    
    # Get quantity and price
    quantity = int(user_input)
    price = float(input("Enter price per unit: $"))
    
    # Calculate total using function
    total = calculate_total(quantity, price)
    
    # Add to grand total
    grand_total += total
    
    # Display item details
    print("\nItem Details:")
    print(f"Quantity: {quantity}")
    print(f"Price per unit: ${price:.2f}")
    if (quantity * price) > 10000.00:
        print(f"Original total: ${quantity * price:.2f}")
        print(f"Discount applied: 10%")
    print(f"Total: ${total:.2f}")

# Display grand total
print("\nSummary:")
print(f"Grand Total: ${grand_total:.2f}")
