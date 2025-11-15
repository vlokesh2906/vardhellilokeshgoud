def format_name(full_name: str) -> str:
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")
    s = full_name.strip()
    if not s:
        return ""
    if "," in s:
        parts = [p.strip() for p in s.split(",", 1)]
        first = parts[1] if len(parts) > 1 else ""
        return f"{parts[0]}, {first}".strip(", ")
    tokens = [t for t in s.split() if t]
    if len(tokens) == 1:
        return tokens[0]
    last = tokens[-1]
    first = " ".join(tokens[:-1])
    return f"{last}, {first}"

if __name__ == "__main__":
    import sys
    try:
        name = input("Enter full name: ")
    except Exception:
        sys.exit(1)
    print(format_name(name))
