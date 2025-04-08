# Function to compute out-the-door price
def compute_out_the_door_price(make, model, ev_code, msrp):
    make = make.lower()
    model = model.lower()
    ev_code = ev_code.upper()
    
    # Determine percent off based on rules
    if make == "honda" and model == "accord":
        discount_percent = 0.10
    elif make == "toyota" and model == "rav4":
        discount_percent = 0.15
    elif ev_code == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05

    # Apply discount
    discount_amount = msrp * discount_percent
    discounted_price = msrp - discount_amount

    # Add 7% tax
    tax = discounted_price * 0.07
    total_price = discounted_price + tax

    return total_price, discount_amount

# Initialize totals
total_msrp = 0
total_sales_price = 0

# Main loop
while True:
    user_input = input("Do you want to enter vehicle data? (Yes or No): ").strip().lower()
    
    if user_input == "yes":
        try:
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            ev_code = input("Is it an electric vehicle? (Y or N): ")
            msrp = float(input("Enter MSRP (sticker price): $"))

            total_price, discount_amount = compute_out_the_door_price(make, model, ev_code, msrp)

            print(f"\nVehicle: {make.title()} {model.title()}")
            print(f"Original MSRP: ${msrp:,.2f}")
            print(f"Discount Amount: -${discount_amount:,.2f}")
            print(f"Final Price with Tax: ${total_price:,.2f}\n")

            total_msrp += msrp
            total_sales_price += total_price

        except ValueError:
            print("Invalid input. Please enter numeric value for MSRP.")
    elif user_input == "no":
        print("\n--- Summary ---")
        print(f"Total MSRP of all vehicles: ${total_msrp:,.2f}")
        print(f"Total Sales Price (after discounts & tax): ${total_sales_price:,.2f}")
        print("Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")
