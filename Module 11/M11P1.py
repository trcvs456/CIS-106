# Function to compute discount amount and discounted price
def calculate_discount(quantity, price, discount_rate):
    total_price = quantity * price
    discount_amount = total_price * (discount_rate / 100)
    discounted_price = total_price - discount_amount
    return [discount_amount, discounted_price]  # Using an array to return both values

# Main part of the program
def main():
    num_entries = int(input("How many purchases do you want to enter? "))

    purchase_list = []  # List to store all purchase summaries

    for i in range(1, num_entries + 1):
        print(f"\n--- Enter data for purchase #{i} ---")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        discount_rate = float(input("Enter discount rate (%): "))

        # Call the function
        result = calculate_discount(quantity, price, discount_rate)
        discount_amount = result[0]
        discounted_price = result[1]

        # Store all data in a dictionary and add it to the list
        purchase_list.append({
            "quantity": quantity,
            "price": price,
            "discount_amount": discount_amount,
            "discounted_price": discounted_price
        })

    # Print Summary
    print("\n===== Purchase Summary =====")
    print(f"{'Qty':<6}{'Price':<10}{'Discount':<12}{'Discounted Total':<18}")
    print("-" * 46)

    for p in purchase_list:
        print(f"{p['quantity']:<6}{p['price']:<10.2f}${p['discount_amount']:<11.2f}${p['discounted_price']:<.2f}")

# Run the main program
main()
