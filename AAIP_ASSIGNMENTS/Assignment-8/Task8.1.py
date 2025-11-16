# Test cases
def test_is_valid_email():
    # Valid emails
    assert is_valid_email("user@example.com") == True
    assert is_valid_email("john.doe@company.co.uk") == True
    assert is_valid_email("a@b.c") == True
    
    # Missing @ or .
    assert is_valid_email("userexample.com") == False
    assert is_valid_email("user@examplecom") == False
    
    # Multiple @
    assert is_valid_email("user@@example.com") == False
    assert is_valid_email("user@exam@ple.com") == False
    
    # Starts with special character
    assert is_valid_email("@user@example.com") == False
    assert is_valid_email(".user@example.com") == False
    
    # Ends with special character
    assert is_valid_email("user@example.com.") == False
    assert is_valid_email("user@example.com@") == False
    
    # Empty string
    assert is_valid_email("") == False
    
    print("All tests passed!")


# Implementation
def is_valid_email(email):
    """
    Validates email based on specific rules.
    
    Rules:
    - Must contain both '@' and '.' characters
    - Must not start or end with a special character
    - Must not contain more than one '@'
    """
    if not email:
        return False
    
    # Check for @ and .
    if email.count('@') != 1 or '.' not in email:
        return False
    
    # Check if starts or ends with special character
    special_chars = '@.'
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    
    return True


# Run tests
if __name__ == "__main__":
    test_is_valid_email()
