from typing import TypeVar, List, Optional

T = TypeVar("T")


def find_first(items: List[T], predicate: callable) -> Optional[T]:
    """
    Generic function that finds first item matching a predicate.
    Returns None if no match is found.
    """
    return next((item for item in items if predicate(item)), None)


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Safely performs division, returning None instead of raising ZeroDivisionError.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


# Example usage
if __name__ == "__main__":
    # find_first examples
    numbers = [1, 3, 5, 6, 7, 8]
    print("Finding first even number:", find_first(numbers, lambda x: x % 2 == 0))

    words = ["hello", "world", "python", "programming"]
    print(
        "Finding first word longer than 6 chars:",
        find_first(words, lambda x: len(x) > 6),
    )

    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35},
    ]
    print("Finding first user over 28:", find_first(users, lambda u: u["age"] > 28))

    # safe_divide examples
    test_cases = [(10.0, 2.0), (10.0, 0.0), (-15.0, 3.0), (8.0, 4.0)]

    for numerator, denominator in test_cases:
        result = safe_divide(numerator, denominator)
        print(f"{numerator} / {denominator} = {result}")
