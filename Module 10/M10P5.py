# Function to compute assessed value based on county
def compute_assessed_value(county, market_value):
    county = county.lower()
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70
    return market_value * percent

# Initialize totals
total_market_value = 0
total_assessed_value = 0

# Main loop
while True:
    user_input = input("Do you want to enter home data? (Yes or No): ").strip().lower()

    if user_input == "yes":
        county = input("Enter the county: ").strip()
        try:
            market_value = float(input("Enter the market value of the home: $"))
            assessed_value = compute_assessed_value(county, market_value)

            print(f"\nCounty: {county.title()}")
            print(f"Market Value: ${market_value:,.2f}")
            print(f"Assessed Value: ${assessed_value:,.2f}\n")

            total_market_value += market_value
            total_assessed_value += assessed_value
        except ValueError:
            print("Invalid input. Please enter a numeric value for market value.")
    elif user_input == "no":
        print("\n--- Summary ---")
        print(f"Total Market Value of All Homes: ${total_market_value:,.2f}")
        print(f"Total Assessed Value of All Homes: ${total_assessed_value:,.2f}")
        print("Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")
