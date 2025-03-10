
# Get user input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

# Initialize variables
total_interest = 0

# Print header
print("\nYear\tBeginning Balance\tEnding Balance")
print("------------------------------------------------")

# Loop through 5 years
for year in range(1, 6):
    interest = principal * rate  # Calculate interest
    ending_balance = principal + interest  # Compute new balance
    
    # Print formatted output
    print(f"{year}\t${principal:,.2f}\t\t${ending_balance:,.2f}")
    
    # Update total interest and principal for next year
    total_interest += interest
    principal = ending_balance

# Print total interest earned
print(f"\nTotal interest earned: ${total_interest:,.2f}")

