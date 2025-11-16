from typing import Iterable, Tuple

def sum_even_odd_manual(numbers: Iterable[int]) -> Tuple[int, int]:
    """Compute the sum of even and odd integers from a list.

    This function iterates over `numbers`, separates even and odd integers,
    and returns their sums as a tuple.

    Args:
        numbers (Iterable[int]): An iterable of integers to process.

    Returns:
        Tuple[int, int]: A 2-tuple (sum_even, sum_odd) where:
            - sum_even is the sum of all even integers in `numbers`.
            - sum_odd is the sum of all odd integers in `numbers`.

    Raises:
        TypeError: If `numbers` is not iterable or contains non-integer items.
    """
    try:
        iter(numbers)
    except TypeError:
        raise TypeError("numbers must be an iterable of integers")

    sum_even = 0
    sum_odd = 0
    for value in numbers:
        if not isinstance(value, int):
            raise TypeError("all items in numbers must be integers")
        if value % 2 == 0:
            sum_even += value
        else:
            sum_odd += value
    return sum_even, sum_odd


def sum_even_odd_ai(numbers: Iterable[int]) -> Tuple[int, int]:
    """Return the sums of even and odd numbers found in the given iterable.

    Scans the provided iterable of integers and accumulates two totals:
    one for even numbers and one for odd numbers. The result is returned
    as (even_total, odd_total).

    Args:
        numbers (Iterable[int]): Sequence or iterable containing integers.

    Returns:
        Tuple[int, int]: (even_total, odd_total)

    Example:
        >>> sum_even_odd_ai([1, 2, 3, 4])
        (6, 4)
    """
    try:
        iter(numbers)
    except TypeError:
        raise TypeError("numbers must be an iterable of integers")

    even_total = 0
    odd_total = 0
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("all items must be integers")
        if n % 2 == 0:
            even_total += n
        else:
            odd_total += n
    return even_total, odd_total


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print("manual:", sum_even_odd_manual(sample))  # (12, 9)
    print("ai:    ", sum_even_odd_ai(sample))      # (12, 9)

# Comparison (short):
# - Manual docstring (Google style) is structured: explicit Args, Returns, and Raises sections,
#   which is good for clarity and tooling that parses Google-style docstrings.
# - AI-generated docstring is more concise and includes an example; it uses plain language
#   and broader type wording (Sequence/Iterable) which may be friendlier but less strict.
