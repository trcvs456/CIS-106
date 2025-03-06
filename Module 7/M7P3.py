# Initial prompt to determine if the user wants to continue
response = input("Do you want to run the program? (Yes to continue): ").strip().lower()

# Initialize counter for number of students
student_count = 0

while response == "yes":
    # Get user input for last name and exam scores
    last_name = input("Enter the student's last name: ").strip()
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))

    # Compute the average exam score
    average_score = (score1 + score2) / 2

    # Display last name and average score
    print(f"Student: {last_name}, Average Score: {average_score:.2f}")

    # Increment the student count
    student_count += 1

    # Prompt the user to run the loop again
    response = input("Do you want to enter another student? (Yes to continue): ").strip().lower()

# Display the total number of students who entered data
print(f"Total number of students entered: {student_count}")
print("Program has ended.")
