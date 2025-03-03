# Initial prompt to determine if the user wants to continue
response = input("Do you want to run the program? (Yes to continue): ").strip().lower()

# Initialize counters and sum variables
employee_count = 0
total_gross_pay = 0.0

while response == "yes":
    # Get user input for employee details
    last_name = input("Enter the employee's last name: ").strip()
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter hourly pay rate: "))

    # Compute gross pay with overtime (time and a half for hours over 40)
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * rate_of_pay) + (overtime_hours * rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay

    # Display employee's last name and gross pay
    print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}")

    # Update total gross pay and employee count
    total_gross_pay += gross_pay
    employee_count += 1

    # Prompt the user to run the loop again
    response = input("Do you want to enter another employee? (Yes to continue): ").strip().lower()

# After the loop, display total gross pay, employee count, and average pay
if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"\nTotal number of employees: {employee_count}")
    print(f"Total gross pay: ${total_gross_pay:.2f}")
    print(f"Average pay: ${average_pay:.2f}")
else:
    print("No employees were entered.")

print("Program has ended.")
