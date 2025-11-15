def is_palindrome(text):
    text = ''.join(e.lower() for e in text if e.isalnum())
    return text == text[::-1]

# Take user input
string = input("Enter a string: ")
if is_palindrome(string):
    print("It is a palindrome")
else:
    print("Not a palindrome")
