# Recursive version of factorial
def factorial_recursive(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative version of factorial
def factorial_iterative(n):
    """Calculate factorial iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Take user input
try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Recursive factorial of {num}: {factorial_recursive(num)}")
        print(f"Iterative factorial of {num}: {factorial_iterative(num)}")
except ValueError:
    print("Please enter a valid integer.")
