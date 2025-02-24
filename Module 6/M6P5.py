# Get employee details
last_name = input("Enter employee's last name: ")
salary = float(input("Enter employee's salary: "))
job_level = int(input("Enter employee's job level: "))
# Determine the bonus rate based on job level
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
# Calculate the bonus
bonus = salary * bonus_rate
# Display results
print("\n--- Employee Bonus Summary ---")
print(f"Employee Last Name: {last_name}")
print(f"Bonus: ${bonus:.2f}")
