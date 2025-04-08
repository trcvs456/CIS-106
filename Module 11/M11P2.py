
# Function to compute total and average exam scores
def compute_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    return [total, average]  # Using an array to return both values

# Main part of the program
def main():
    num_students = int(input("How many students do you want to enter? "))
    student_list = []  # List to hold results for all students

    for i in range(1, num_students + 1):
        print(f"\n--- Enter data for student #{i} ---")
        last_name = input("Enter student's last name: ")
        
        scores = []
        for j in range(1, 4):
            score = float(input(f"Enter exam score {j}: "))
            scores.append(score)

        result = compute_scores(scores)
        total_points = result[0]
        average_score = result[1]

        # Store result in list
        student_list.append({
            "last_name": last_name,
            "total_points": total_points,
            "average_score": average_score
        })

    # Print summary
    print("\n===== Student Summary =====")
    print(f"{'Last Name':<15}{'Total Points':<15}{'Average Score':<15}")
    print("-" * 45)
    for student in student_list:
        print(f"{student['last_name']:<15}{student['total_points']:<15.2f}{student['average_score']:<15.2f}")

# Run the main program
main()
