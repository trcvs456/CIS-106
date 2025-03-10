# Number of terms to display
n = 20

# Initialize first two numbers
a, b = 0, 1

# Print Fibonacci sequence
print("First 20 Fibonacci numbers:")
for _ in range(n):
    print(a, end=" ")  # Print the current number
    a, b = b, a + b  # Update values for next iteration

print()  # New line after sequence
