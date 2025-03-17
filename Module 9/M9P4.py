
# Function to determine pay rate based on job code
def get_pay_rate(job_code):
    job_rates = {
        'L': 25.00,
        'A': 30.00,
        'J': 50.00
    }
    return job_rates.get(job_code.upper(), 0.0)

# Initialize total gross pay
total_gross_pay = 0.0

print("Employee Pay Calculator")
print("Enter 'q' for last name to quit")

# Loop for user to enter multiple employees
while True:
    print("\nEnter employee details:")
    last_name = input("Enter last name (or 'q' to quit): ")
    
    # Check if user wants to quit
    if last_name.lower() == 'q':
        break
    
    # Get job code and hours
    job_code = input("Enter job code (L, A, or J): ")
    hours = float(input("Enter hours worked: "))
    
    # Get pay rate using function
    rate = get_pay_rate(job_code)
    
    # Calculate gross pay with overtime
    if hours <= 40:
        gross_pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    
    # Add to total gross pay
    total_gross_pay += gross_pay
    
    # Display employee details
    print(f"\nEmployee: {last_name}")
    print(f"Gross Pay: ${gross_pay:.2f}")

# Display total gross pay
print(f"\nTotal Gross Pay for all employees: ${total_gross_pay:.2f}")
