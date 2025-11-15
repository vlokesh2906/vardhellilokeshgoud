def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Take user input
text = input("Enter a string: ")
if is_palindrome(text):
    print("It is a palindrome")
else:
    print("Not a palindrome")
