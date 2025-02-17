#enter meal total
meal_total=float(input("Enter total amount of meal:"))
fifteen_percent=0.15
fifteen_tip=meal_total*fifteen_percent
fifteen_total=fifteen_tip+meal_total
eighteen_percent=0.18
eighteen_tip=meal_total*eighteen_percent
eighteen_total=meal_total+eighteen_tip
twenty_percent=0.20
twenty_tip=meal_total*twenty_percent
twenty_total=meal_total+twenty_tip
#display total amount of meal
#display the tip amount of meal
#display the total of meal including tip amount
print(f"With 15% Tip:")
print(f"    Total:".ljust(20),"${:10.2f}".rjust(10).format(meal_total))
print(f"    Tip: ".ljust(20),"${:10.2f}".rjust(10).format(fifteen_tip))
print(f"    Total with tip: ".ljust(20),"${:10.2f}".rjust(10).format(fifteen_total))
print(f"With 18% Tip:")
print(f"    Total: " .ljust(20),"${:10.2f}".rjust(10).format(meal_total))
print(f"    Tip:" .ljust(20),"${:10.2f}".rjust(10).format(eighteen_tip))
print(f"    Total with tip:".ljust(20),"${:10.2f}".rjust(10).format(eighteen_total))
print(f"With 20% Tip:")
print(f"    Total: ".ljust(20),"${:10.2f}".rjust(10).format(meal_total))
print(f"    Tip:".ljust(20),"${:10.2f}".rjust(10).format(twenty_tip))
print(f"    Total with tip:" .ljust(20),"${:10.2f}".rjust(10).format(twenty_total))

