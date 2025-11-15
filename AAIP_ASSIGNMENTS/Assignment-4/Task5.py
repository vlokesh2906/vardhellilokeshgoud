def count_lines(filename: str) -> int:
    """
    Count the number of lines in a text file.
    
    Examples:
    - "empty.txt" (empty file) → 0 lines
    - "single.txt" (one line) → 1 line
    - "multiline.txt" (multiple lines with empty lines) → actual line count
    
    Returns:
    - int: Number of lines in file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

if __name__ == "__main__":
    try:
        filename = input("Enter the path to your text file: ")
        line_count = count_lines(filename)
        print(f"Number of lines in {filename}: {line_count}")
    except Exception as e:
        print(f"Error: {e}")
