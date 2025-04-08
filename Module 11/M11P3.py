# Function to compute commission and next year's sales target
def calculate_sales_info(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 1.05  # 5% increase
    return [commission, next_year_target]  # Using an array to return both values

# Main part of the program
def main():
    num_salespeople = int(input("How many salespeople do you want to enter? "))

    sales_report = []  # List to store all results

    for i in range(1, num_salespeople + 1):
        print(f"\n--- Enter data for salesperson #{i} ---")
        last_name = input("Enter salesperson's last name: ")
        sales = float(input("Enter total sales amount: $"))

        # Call the function
        result = calculate_sales_info(sales)
        commission = result[0]
        next_year_target = result[1]

        # Store data in a dictionary
        sales_report.append({
            "last_name": last_name,
            "commission": commission,
            "next_year_target": next_year_target
        })

    # Print Summary
    print("\n===== Sales Report Summary =====")
    print(f"{'Last Name':<15}{'Commission':<15}{'Next Year Target':<20}")
    print("-" * 50)
    for entry in sales_report:
        print(f"{entry['last_name']:<15}${entry['commission']:<14.2f}${entry['next_year_target']:<.2f}")

# Run the main program
main()
