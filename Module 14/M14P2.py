class Student:
    # Dictionary for district tuition rates
    tuition_rates = {
        'I': 250.00,   # In-district
        'O': 500.00,   # Out-of-district
        'G': 250.00    # Reciprocity (same as in-district)
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        # Use dictionary to get rate; default to $500.00 if code is not found
        rate = Student.tuition_rates.get(self.district_code, 500.00)
        return self.enrolled_credits * rate

    def generate_report(self):
        tuition = self.compute_tuition()
        print("\n----- Student Tuition Summary Report -----")
        print(f"Name:            {self.first_name} {self.last_name}")
        print(f"District Code:   {self.district_code}")
        print(f"Credit Hours:    {self.enrolled_credits}")
        print(f"Tuition Owed:    ${tuition:,.2f}")
        print("------------------------------------------")

# Instantiate one student for each district code
students = [
    Student("Ava", "Anderson", "I", 12),   # In-district
    Student("Ben", "Brown", "O", 15),      # Out-of-district
    Student("Dana", "Davis", "G", 6)       # Reciprocity
]

# Generate reports for all students
for student in students:
    student.generate_report()
