# Base class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")

# Derived class Manager
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def long_term_bonus(self):
        return self.salary * 0.40

# Create two employee objects and two manager objects
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 55000)
manager1 = Manager("Charlie", 80000)
manager2 = Manager("Diana", 90000)

# Display info for employees
employee1.display_info()
employee2.display_info()

# Display info for managers and their long-term bonus
manager1.display_info()
print(f"Long-term bonus for {manager1.name}: ${manager1.long_term_bonus()}")

manager2.display_info()
print(f"Long-term bonus for {manager2.name}: ${manager2.long_term_bonus()}")

