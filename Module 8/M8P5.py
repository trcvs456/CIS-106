# Function to calculate bonus based on salary
def calculate_bonus(salary):
    if salary >= 100000:
        rate = 0.20  # 20% bonus for salaries $100,000 and above
    elif salary >= 50000:
        rate = 0.15  # 15% bonus for salaries $50,000 and above
    else:
        rate = 0.10  # 10% bonus for all other salaries
    return salary * rate

# Initialize total bonus accumulator
total_bonus = 0

# Print header for output
print("Employee Bonus Report")
print("---------------------")

# Open and read the file containing employee data
with open("employee_data.txt", "r") as file:
    lines = file.readlines()
    
    # Process each employee record (assuming each record is 2 lines)
    for i in range(0, len(lines), 2):
        last_name = lines[i].strip()              # Employee's last name
        salary = float(lines[i + 1].strip())        # Salary as a float
        bonus = calculate_bonus(salary)             # Compute bonus
        
        # Display the employee's data
        print(f"{last_name}: Salary = ${salary:,.2f}, Bonus = ${bonus:,.2f}")
        
        # Add the bonus to the total
        total_bonus += bonus

# Display total bonus paid out after processing all employees
print("---------------------")
print(f"Total Bonus Paid Out: ${total_bonus:,.2f}")

