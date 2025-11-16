"""
calculator module providing basic arithmetic operations.
Save as calculator.py (or use this content in task_3.py).
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First addend.
    b : int or float
        Second addend.

    Returns
    -------
    int or float
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The difference a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First factor.
    b : int or float
        Second factor.

    Returns
    -------
    int or float
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.

    Returns
    -------
    float
        The quotient a / b.

    Raises
    ------
    ValueError
        If b == 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # sample inputs
    a, b = 4, 2
    print(f"add({a}, {b}) = {add(a, b)}")
    print(f"subtract({a}, {b}) = {subtract(a, b)}")
    print(f"multiply({a}, {b}) = {multiply(a, b)}")
    print(f"divide({a}, {b}) = {divide(a, b)}")
