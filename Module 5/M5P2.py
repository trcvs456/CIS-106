# Get input for item and quantity
item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))
# Determine unit price based on item
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00
# Calculate extended price
extended_price = quantity * unit_price
# Display results
print("\nOrder Details:")
print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
