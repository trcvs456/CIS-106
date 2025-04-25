# Create dictionary with student names and grades
students_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88
}

# Print the student names and grades with headers
print(f"{'Student Name':<15}{'Grade'}")
for student, grade in students_grades.items():
    print(f"{student:<15}{grade}")

# Calculate and print the class average
class_average = sum(students_grades.values()) / len(students_grades)
print(f"\nClass Average: {class_average:.2f}")
