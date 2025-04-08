# Function to compute ticket price based on miles
def compute_ticket_price(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles <= 29:
        return 10
    elif 10 <= miles <= 19:
        return 8
    else:
        return 5

# Initialize total ticket price
total_price = 0

# Main loop
while True:
    user_input = input("Do you want to enter train ticket info? (Yes or No): ").strip().lower()

    if user_input == "yes":
        last_name = input("Enter your last name: ")
        try:
            miles = int(input("Enter miles from downtown Chicago: "))
            ticket_price = compute_ticket_price(miles)
            print(f"{last_name}, your train ticket price is: ${ticket_price:.2f}")
            total_price += ticket_price
        except ValueError:
            print("Please enter a valid number for miles.")
    elif user_input == "no":
        print(f"\nTotal of all ticket prices: ${total_price:.2f}")
        print("Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")
