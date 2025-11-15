from typing import Iterable

def sum_of_squares(nums: Iterable[float]) -> float:
    """
    Return the sum of squares of numeric values in nums.
    Non-numeric values are ignored. Accepts any iterable of values.
    """
    total = 0.0
    for x in nums:
        try:
            n = float(x)
        except (TypeError, ValueError):
            continue
        total += n * n
    return total

if __name__ == "__main__":
    raw = input("Enter numbers (comma or space separated), or press Enter to use sample [1,2,3,4]: ").strip()
    if raw:
        parts = raw.replace(',', ' ').split()
        try:
            nums = [float(p) for p in parts]
        except ValueError:
            print("Invalid input — please enter numbers only.")
            raise SystemExit(1)
    else:
        nums = [1, 2, 3, 4]

    print(f"Numbers: {nums}")
    print("Sum of squares:", sum_of_squares(nums))
