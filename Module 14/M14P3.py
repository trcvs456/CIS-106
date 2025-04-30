class Student:
    # Dictionary for district tuition rates
    tuition_rates = {
        'I': 250.00,   # In-district
        'O': 500.00,   # Out-of-district
        'X': 800.00,   # International
        'G': 250.00    # Reciprocity
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        # Default to $500.00 if code not found
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
    Student("Tracy","Ruiz", "I", 12), #in-district
    Student("John","Trance", "O", 15), # out-of-district
    Student("Lina","George", "X", 9), #international
    Student("Alex","Howard", "G", 6) #reciprocity
]

# Generate reports for all students
for student in students:
    student.generate_report()

