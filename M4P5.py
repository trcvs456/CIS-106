#enter fixed cost
fixed_cost=float(input("Fixed cost:"))
#enter price per unit
price_per_unit=float(input("Price per unit:"))
#enter cost per unit
cost_per_unit=float(input("Cost per unit:"))
#calculate break-even point( I used replit for lines 8 and 9)
unit_contribution_margin= price_per_unit-cost_per_unit
break_even_point=fixed_cost/unit_contribution_margin
#display break even point in units 
print(f"Break-even point: {break_even_point:.0f} units")
                     
                     
