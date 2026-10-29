"""Demonstrate Python's str.replace() method."""


def replace_all(text, old, new):
    """Replace every occurrence of `old` with `new`."""
    return text.replace(old, new)


def replace_first(text, old, new, count=1):
    """Replace only the first `count` occurrences of `old` with `new`."""
    return text.replace(old, new, count)


def replace_ignore_case(text, old, new):
    """Replace `old` with `new` regardless of letter case."""
    result = []
    lower_text = text.lower()
    lower_old = old.lower()
    start = 0
    while True:
        index = lower_text.find(lower_old, start)
        if index == -1 or not old:
            result.append(text[start:])
            break
        result.append(text[start:index])
        result.append(new)
        start = index + len(old)
    return "".join(result)


def main():
    food = "Burger"
    print(f"Original:             {food}")

    # Replace every "r" with "s"
    print(f"Replace all 'r':      {replace_all(food, 'r', 's')}")    # Busges

    # Replace only the first "r"
    print(f"Replace first 'r':    {replace_first(food, 'r', 's')}")  # Busger

    # replace() is case-sensitive, so "b" does not match "B"
    print(f"Replace 'b' (case):   {replace_all(food, 'b', 'x')}")    # Burger

    # Case-insensitive replacement
    print(f"Replace 'b' (nocase): {replace_ignore_case(food, 'b', 'x')}")  # xurger

    # Strings are immutable: replace() returns a new string
    food.replace("r", "s")
    print(f"Unassigned replace:   {food}")                           # Burger
    food = food.replace("r", "s")
    print(f"Assigned replace:     {food}")                           # Busges


if __name__ == "__main__":
    main()
