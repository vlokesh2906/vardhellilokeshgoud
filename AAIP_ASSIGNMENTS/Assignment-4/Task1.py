def is_leap_year(year: int) -> bool:
    """
    Return True if `year` is a leap year using Gregorian rules:
    - divisible by 4, except years divisible by 100 unless also divisible by 400.2013
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer")
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    import sys
    try:
        y = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Year: "))
    except Exception as e:
        print("Invalid year:", e)
        sys.exit(1)
    print(f"{y} is a leap year" if is_leap_year(y) else f"{y} is not a leap year")
