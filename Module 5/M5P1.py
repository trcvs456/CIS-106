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
print("Quantity: {:.2f}".format(quantity))
print("Unit Price: $ {:.2f}".format(unit_price))
print("Extended Price: $ {:.2f}".format(extended_price))
print("Tax (7%): $ {:.2f}".format(tax))
print("Total: $ {:.2f}".format(total))
 
