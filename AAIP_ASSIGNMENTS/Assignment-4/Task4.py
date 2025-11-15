def count_vowels_zero(text: str) -> int:
    """Count vowels in given string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return sum(1 for c in text.lower() if c in 'aeiou')

# Few-shot approach with examples
def count_vowels_few(text: str) -> int:
    """Count vowels in text.
    Examples:
    - "hello" → 2 (e,o)
    - "PYTHON" → 1 (o)
    - "sky" → 0
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return sum(c in 'aeiou' for c in text.lower())

if __name__ == "__main__":
    try:
        text = input("Enter text to count vowels: ")
        print(f"Zero-shot result: {count_vowels_zero(text)} vowels")
        print(f"Few-shot result: {count_vowels_few(text)} vowels")
    except Exception as e:
        print(f"Error: {e}")
