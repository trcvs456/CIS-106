#input the amount of widgets
quantity = input("Enter the quantity of widgets: ")
# I used replit for line 4 and 5
if quantity.isdigit():
    quantity = int(quantity)
    
    if quantity > 10000:
        price = 10
    elif 5000 <= quantity <= 10000:
        price = 20
    else:
        price = 30
# calcute extended price, tax amount, and total 
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax
#display extended price, tax amount, and total
print(f"\nExtended Price: ${extended_price:.2f}")
print(f"Tax Amount (7%): ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")

  
