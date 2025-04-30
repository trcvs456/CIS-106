class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, rate):
        bonus = self.salary * rate
        return bonus

# Create an employee object
employee1 = Employee("Tracy", 60000)

# Ask user for bonus rate
bonus_rate = float(input("Enter bonus rate (e.g., 0.1 for 10%): "))

# Calculate and display the bonus
bonus = employee1.calculate_bonus(bonus_rate)
print(f"{employee1.name}'s bonus is: ${bonus:.2f}")
