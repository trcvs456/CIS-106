# Function to compute average score and average with handicap
def compute_bowling_averages(scores, handicap):
    average = sum(scores) / len(scores)
    average_with_handicap = average + handicap
    return [average, average_with_handicap]  # Using a list to return both

# Main part of the program
def main():
    num_bowlers = int(input("How many bowlers do you want to enter? "))
    bowler_list = []  # To store each bowler’s results

    for i in range(1, num_bowlers + 1):
        print(f"\n--- Enter data for bowler #{i} ---")
        last_name = input("Enter bowler's last name: ")
        scores = []

        for j in range(1, 4):
            score = float(input(f"Enter game {j} score: "))
            scores.append(score)

        handicap = float(input("Enter handicap: "))

        # Call the function
        result = compute_bowling_averages(scores, handicap)
        avg_score = result[0]
        avg_with_handicap = result[1]

        # Store in a dictionary
        bowler_list.append({
            "last_name": last_name,
            "average": avg_score,
            "average_with_handicap": avg_with_handicap})

    # Print Summary
    print("\n===== Bowling Summary =====")
    print(f"{'Last Name':<15}{'Avg Score':<15}{'Avg + Handicap':<20}")
    print("-" * 50)
    for b in bowler_list:
        print(f"{b['last_name']:<15}{b['average']:<15.2f}{b['average_with_handicap']:<.2f}")

# Run the program
main()
