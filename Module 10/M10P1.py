# Function to compute next month's sales forecast
def forecast_sales(month, sales):
    # Convert month to lowercase to handle case insensitivity
    month = month.lower()

    # Define forecast percentages
    if month in ["jan", "feb", "mar"]:
        forecast_percent = 0.10
    elif month in ["apr", "may", "jun"]:
        forecast_percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        forecast_percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        forecast_percent = 0.25
    else:
        print("Invalid month entered. Forecast cannot be computed.")
        return None

    # Calculate next month's sales
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

# Main loop
while True:
    user_input = input("Do you want to enter sales data? (Yes or No): ").strip().lower()
    
    if user_input == "yes":
        last_name = input("Enter your last name: ")
        month = input("Enter the month (e.g., Jan, Feb, etc.): ")
        try:
            sales = float(input("Enter the sales amount: "))
            forecast = forecast_sales(month, sales)
            if forecast is not None:
                print(f"Hi {last_name}, your forecasted sales for next month is: ${forecast:.2f}")
        except ValueError:
            print("Invalid input for sales. Please enter a numeric value.")
    elif user_input == "no":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")



