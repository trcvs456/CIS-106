# Get input for quantity
quantity=int(input("Enter the quantity of items:"))
# Determine unit price based on quantity
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
# Calculate costs
extended_price=quantity*unit_price
tax= extended_price*0.07
total= extended_price+tax
# Display results (Note to professor: "I tried the way you said in class with float instead of "f" but it wont run that way on my computer 
print("\nOrder Summary:")
print(f"Quantity: {quantity:.2f}")
print(f"Unit Price: $ {unit_price:.2f}")
print(f"Extended Price: $ {extended_price:.2f}")
print(f"Tax (7%): $ {tax:.2f}")
print(f"Total: $ {total:.2f}")
 
