from collections.abc import MutableSequence
from typing import Any, Iterator


class OrderedList(MutableSequence):
    """
    A list that maintains its elements in sorted order automatically.
    Implements the MutableSequence abstract base class.
    """

    def __init__(self):
        self._items = []

    def __len__(self) -> int:
        """Returns the number of items in the list."""
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        """Retrieves item at given index."""
        return self._items[index]

    def __setitem__(self, index: int, value: Any) -> None:
        """Sets item at index and maintains sort order."""
        self._items[index] = value
        self._items.sort()

    def __delitem__(self, index: int) -> None:
        del self._items[index]

    def insert(self, index: int, value: Any) -> None:
        """Inserts value at index and maintains sort order."""
        self._items.insert(index, value)
        self._items.sort()

    def __iter__(self) -> Iterator:
        return iter(self._items)


# Usage
ordered = OrderedList()
ordered.extend([3, 1, 4, 1, 5, 9])
print(list(ordered))  # Will be sorted automatically
