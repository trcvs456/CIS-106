# Get user input for the number of books and cost per book
num_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))
# Calculate order total
order_total = num_books * cost_per_book
# Determine shipping cost
shipping_cost = 0 if order_total > 50 else 25
# Display results using format()instead of old method. I believe this should work
print("Order Total: ${:.2f}".format(order_total))
print("Shipping Charge: ${:.2f}".format(shipping_cost))
