# Get user input for principle amount and years to maturity
principle = float(input("Enter the principle amount: "))
years_to_maturity = int(input("Enter years to maturity: "))
# Determine interest rate based on conditions
if principle > 100000 and years_to_maturity == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and years_to_maturity == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and years_to_maturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
# Calculate first year interest
interest_amount = principle * interest_rate
# Display results formatted to two decimal places
print("Principle: ${:.2f}".format(principle))
print("Interest Rate: {:.2f}%".format(interest_rate * 100))
print("First Year Interest: ${:.2f}".format(interest_amount))



