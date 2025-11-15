def find_largest(numbers):
    """Return the largest number in a list."""
    if not numbers:
        return None  # Handle empty list
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# Take user input
try:
    user_input = input("Enter numbers separated by spaces: ")
    num_list = [float(x) for x in user_input.split()]
    if not num_list:
        print("List is empty. Please enter at least one number.")
    else:
        largest = find_largest(num_list)
        print(f"The largest number in the list is: {largest}")
except ValueError:
    print("Please enter valid numbers.")

# Assessment:
# - The function uses a single pass (O(n)), which is efficient for this task.
# - Handles empty list input gracefully.
# - Uses float conversion for broader numeric input support.
# - Code is readable and well-commented.
