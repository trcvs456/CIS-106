# Global variables to store results
results = []

# Function to compute total and tax
def compute_total_and_tax(quantity, unit_price):
    global results  # Use global list to store results
    total = quantity * unit_price  # Calculate total
    tax = total * 0.07  # Calculate tax (7% of total)
    # Append the result as a dictionary to the global list
    results.append({
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total,
        "tax": tax
    })

# Main part of the program
def main():
    num_items = int(input("How many items do you want to enter? "))  # Get number of items

    # Loop through to get data for each item
    for i in range(1, num_items + 1):
        print(f"\n--- Enter data for item #{i} ---")
        quantity = int(input("Enter quantity of the item: "))
        unit_price = float(input("Enter unit price of the item: $"))

        # Call the function to compute total and tax
        compute_total_and_tax(quantity, unit_price)

    # Print Summary
    print("\n===== Item Summary =====")
    print(f"{'Item #':<10}{'Quantity':<10}{'Unit Price':<15}{'Total':<15}{'Tax':<10}")
    print("-" * 60)

    # Display results stored in the global list
    for i, item in enumerate(results, start=1):
        print(f"{i:<10}{item['quantity']:<10}{item['unit_price']:<15.2f}${item['total']:<15.2f}${item['tax']:<10.2f}")

# Run the main program
main()
