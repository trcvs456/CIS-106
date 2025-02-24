# Get the number of concert tickets from the user
num_tickets = int(input("Enter the number of concert tickets: "))
# Calculate the price per ticket based on quantity
if num_tickets >= 25:
    price_per_ticket = 50
elif num_tickets >= 10:
    price_per_ticket = 60
elif num_tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 80
# Calculate the total cost
total_cost = num_tickets * price_per_ticket
# Display results
print(f"Number of Tickets: {num_tickets}")
print(f"Price Per Ticket: ${price_per_ticket}")
print(f"Total Cost: ${total_cost}")
