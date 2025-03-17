
# Function to calculate tuition
def calculate_tuition(credit_hours, district_code):
    rates = {
        'I': 250.00,  # In district rate
        'O': 550.00   # Out of district rate
    }
    rate = rates.get(district_code.upper(), 0.0)
    return credit_hours * rate

# Initialize total tuition
total_tuition = 0.0

print("Student Tuition Calculator")
print("Enter 'q' for last name to quit")

# Loop for user to enter multiple students
while True:
    print("\nEnter student details:")
    last_name = input("Enter last name (or 'q' to quit): ")
    
    # Check if user wants to quit
    if last_name.lower() == 'q':
        break
    
    # Get credit hours and district code
    credit_hours = float(input("Enter credit hours: "))
    district_code = input("Enter district code (I for In-district, O for Out-of-district): ")
    
    # Calculate tuition using function
    tuition = calculate_tuition(credit_hours, district_code)
    
    # Add to total tuition
    total_tuition += tuition
    
    # Display student details
    print(f"\nStudent: {last_name}")
    print(f"Tuition Owed: ${tuition:.2f}")

# Display total tuition
print(f"\nTotal Tuition Owed: ${total_tuition:.2f}")
