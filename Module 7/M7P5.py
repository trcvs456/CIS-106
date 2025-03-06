# Initial prompt to determine if the user wants to continue
response = input("Do you want to run the program? (Yes to continue): ").strip().lower()

# Initialize sum variable for total discount amount
total_discount_amount = 0.0

while response == "yes":
    # Get user input for quantity and price per item
    quantity = int(input("Enter the quantity of the item: "))
    price_per_item = float(input("Enter the price per item: "))

    # Compute extended price
    extended_price = quantity * price_per_item

    # Determine discount percentage based on extended price
    if extended_price > 10000.00:
        discount_percent = 0.25  # 25% discount
    else:
        discount_percent = 0.10  # 10% discount

    # Compute discount amount and total price after discount
    discount_amount = extended_price * discount_percent
    total_price = extended_price - discount_amount

    # Display order details
    print(f"\nOrder Summary:")
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total Price After Discount: ${total_price:.2f}\n")

    # Sum the discount amount
    total_discount_amount += discount_amount

    # Prompt the user to run the loop again
    response = input("Do you want to enter another order? (Yes to continue): ").strip().lower()

# After the loop, display the sum of all discounts
print(f"\nTotal Discount Given Across All Orders: ${total_discount_amount:.2f}")
print("Program has ended.")
