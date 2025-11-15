def cm_to_inches(cm: float) -> float:
    """
    Convert centimeters to inches (1 inch = 2.54 cm) and print a conversion log.

    One-shot example:
    input: 30
    printed output: Converted 30.0 cm to 11.8110 inches
    """
    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number")
    inches = cm / 2.54
    print(f"Converted {float(cm)} cm to {inches:.4f} inches")
    return inches
# ...existing code...

if __name__ == "__main__":
    import sys
    try:
        # Accept cm from command-line or prompt the user
        cm = float(sys.argv[1]) if len(sys.argv) > 1 else float(input("Centimeters: "))
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)

    cm_to_inches(cm)
