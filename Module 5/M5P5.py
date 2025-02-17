# Get user input
last_name = input("Enter your last name: ")
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents: "))
# Compute adjusted gross income
adjusted_gross_income = gross_income - (num_dependents * 12000)
# Determine income tax rate
tax_rate = 0.20 if adjusted_gross_income > 50000 else 0.10
# Compute income tax
income_tax = adjusted_gross_income * tax_rate
# Ensure minimum tax is $100
if income_tax < 0:
    income_tax = 100
# Display results
print("\nLast Name: {}".format(last_name))
print("Gross Income: ${:.2f}".format(gross_income))
print("Number of Dependents: {}".format(num_dependents))
print("Adjusted Gross Income: ${:.2f}".format(adjusted_gross_income))
print("Income Tax: ${:.2f}".format(income_tax))
