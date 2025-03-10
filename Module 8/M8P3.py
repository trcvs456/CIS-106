# Function to calculate bonus based on salary
def calculate_bonus(salary):
    if salary >= 100000:
        return salary * 0.20  # 20% bonus for salaries $100,000 and up
    elif salary >= 50000:
        return salary * 0.15  # 15% bonus for salaries $50,000
    else:
        return salary * 0.10  # 10% bonus for salaries less than $50,000

# Open the text file with employee data
with open('employee_data.txt', 'r') as file:
    total_bonus = 0
    print("Last Name\tSalary\t\tBonus")
    print("----------------------------------------")
    
    # Read through the file line by line
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        last_name = lines[i].strip()  # Read the last name
        salary = float(lines[i + 1].strip())  # Read the salary and convert to float
        bonus = calculate_bonus(salary)  # Calculate the bonus
        
        # Display employee data
        print(f"{last_name}\t\t${salary:,.2f}\t${bonus:,.2f}")
        
        # Add the bonus to the total bonus
        total_bonus += bonus

    # After the loop, display the total bonus paid out
    print("\nTotal Bonus Paid Out: ${:,.2f}".format(total_bonus))




