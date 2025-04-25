# Create a dictionary with student names as keys and a list of grades as values
students_grades = {
    "Alice": [85, 88, 91],
    "Bob": [92, 89, 94],
    "Charlie": [78, 80, 85],
    "Diana": [88, 91, 90]
}

# Function to calculate average of each student
def calculate_averages(grades_dict):
    averages = {}
    for student, grades in grades_dict.items():
        avg = sum(grades) / len(grades)
        averages[student] = avg
    return averages

# Get average grades for the class
averages = calculate_averages(students_grades)

# Print the student names, grade averages, and class average for each grade
print(f"{'Student Name':<15}{'Grade Average'}")
for student, average in averages.items():
    print(f"{student:<15}{average:.2f}")

# Calculate and print class averages for each grade
class_averages = [sum(grade[i] for grade in students_grades.values()) / len(students_grades) for i in range(3)]

print("\nClass Averages for Each Grade:")
for i, class_avg in enumerate(class_averages, 1):
    print(f"Grade {i} Average: {class_avg:.2f}")
