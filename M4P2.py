#enter the purchase price per stock
price_per_share=int(input("Enter the price per share:"))
#enter the current stock price
current_stock_price=int(input("Enter current stock price:"))
#enter the quantity of stocks 
quantity_stock=float(input("Enter the quantity of stocks:"))
#compute current stock price minus price per share, times quantity of stocks
value= (current_stock_price - price_per_share) * quantity_stock
#display the total 
print(f"The value of the stock: ${value:,.2f} (If the amount is negative you are losing money)")




                      

                      
                      
