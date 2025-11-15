def reverse_string(s):
    """Return the reversed string."""
    return s[::-1]

# Take user input
user_input = input("Enter a string to reverse: ")
reversed_str = reverse_string(user_input)
print(f"Reversed string: {reversed_str}")
