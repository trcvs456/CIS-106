# Function to load data from file into parallel arrays
def load_data(filename):
    last_names = []
    exam_scores = []
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split()
            last_names.append(name)
            exam_scores.append(int(score))
    return last_names, exam_scores

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

# Function to find and display highest and lowest scores
def display_highest_and_lowest(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"\nHighest Score: {names[high_index]} - {high_var}")
    print(f"Lowest Score: {names[low_index]} - {low_var}")

# Main program logic
filename = "names.txt"
last_names, exam_scores = load_data(filename)

display_names_and_scores(last_names, exam_scores)
print()
display_names_and_scores_reverse(last_names, exam_scores)
display_highest_and_lowest(last_names, exam_scores)
