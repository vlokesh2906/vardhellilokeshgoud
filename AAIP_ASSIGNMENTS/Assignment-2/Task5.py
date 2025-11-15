import re
from typing import Iterable, List, Dict

def parse_ints_from_string(s: str) -> List[int]:
    """
    Parse integers from a string containing numbers separated by commas/spaces.
    Non-integer tokens are ignored.
    """
    if not s:
        return []
    parts = re.split(r'[,\s]+', s.strip())
    ints: List[int] = []
    for p in parts:
        if p == '':
            continue
        try:
            ints.append(int(p))
        except ValueError:
            # ignore tokens that are not integers
            continue
    return ints

def sum_even_odd(nums: Iterable[int]) -> Dict[str, int]:
    """
    Compute sums of even and odd integers in a single pass.
    Returns {"even": sum_of_evens, "odd": sum_of_odds}.
    """
    even_sum = 0
    odd_sum = 0
    for n in nums:
        try:
            i = int(n)
        except (TypeError, ValueError):
            continue
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return {"even": even_sum, "odd": odd_sum}

if __name__ == "__main__":
    raw = input("Enter integers (comma or space separated), or press Enter to use [1 2 3 4 5 6]: ").strip()
    if raw:
        numbers = parse_ints_from_string(raw)
        if not numbers:
            print("No valid integers parsed. Exiting.")
        else:
            res = sum_even_odd(numbers)
            print(f"Numbers: {numbers}")
            print(f"Sum of even numbers: {res['even']}")
            print(f"Sum of odd numbers:  {res['odd']}")
    else:
        sample = [1, 2, 3, 4, 5, 6]
        res = sum_even_odd(sample)
        print(f"Sample Numbers: {sample}")
        print(f"Sum of even numbers: {res['even']}")
        print(f"Sum of odd numbers:  {res['odd']}")
