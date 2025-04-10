# Parallel arrays: last names and exam scores
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

exam_scores = [88, 92, 79, 85, 90, 76, 84, 95, 89, 91]

# Function to display names and scores in original order
def display_names_and_scores(names, scores):
    print("Names and Exam Scores (Original Order):")
    for i in range(len(names)):
        print(f"{names[i]} - Score: {scores[i]}")

# Function to display names and scores in reverse order
def display_names_and_scores_reverse(names, scores):
    print("Names and Exam Scores (Reverse Order):")
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]} - Score: {scores[i]}")

# Call the functions
display_names_and_scores(last_names, exam_scores)
print()  # Blank line for spacing
display_names_and_scores_reverse(last_names, exam_scores)
