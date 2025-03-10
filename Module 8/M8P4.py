# Function to compute extended price (quantity * price)
def calculate_extended_price(quantity, price):
    return quantity * price

# Open the text file with item, quantity, and price data
with open('order_data.txt', 'r') as file:
    total_extended_price = 0
    total_orders = 0
    order_count = 0

    print("Item\t\tQuantity\tPrice\t\tExtended Price")
    print("--------------------------------------------------------")
    
    # Read through the file line by line
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        item = lines[i].strip()  # Read the item name
        quantity = int(lines[i + 1].strip())  # Read the quantity and convert to integer
        price = float(lines[i + 2].strip())  # Read the price and convert to float
        extended_price = calculate_extended_price(quantity, price)  # Calculate extended price
        
        # Display item details
        print(f"{item}\t\t{quantity}\t\t${price:,.2f}\t${extended_price:,.2f}")
        
        # Update the totals
        total_extended_price += extended_price
        order_count += 1
    
    # After the loop, display the summary
    print("\nTotal Extended Price: ${:,.2f}".format(total_extended_price))
    print(f"Total Number of Orders: {order_count}")
    print("Average Order Price: ${:,.2f}".format(total_extended_price / order_count if order_count > 0 else 0))
