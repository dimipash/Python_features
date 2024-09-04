"""
This code demonstrates the use of generic types in Python.
Generic types allow you to define a type that can be used with any data type.
In this example, the Stack class is a generic type that can be used with any data type.
The get_first_item and create_dict functions are also generic types that can be used with any data type.
"""

from typing import Generic, TypeVar, List, Dict, Optional

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> Optional[T]:
        return self.items[-1] if self.items else None

    def is_empty(self) -> bool:
        return len(self.items) == 0


def get_first_item(container: List[T]) -> Optional[T]:
    return container[0] if container else None


def create_dict(keys: List[K], values: List[V]) -> Dict[K, V]:
    return dict(zip(keys, values))


if __name__ == "__main__":
    # Using the generic Stack class
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Top of int_stack: {int_stack.peek()}")

    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Top of str_stack: {str_stack.peek()}")

    # Using the generic get_first_item function
    int_list: List[int] = [1, 2, 3]
    str_list: List[str] = ["a", "b", "c"]
    print(f"First item of int_list: {get_first_item(int_list)}")
    print(f"First item of str_list: {get_first_item(str_list)}")

    # Using the generic create_dict function
    keys: List[str] = ["a", "b", "c"]
    values: List[int] = [1, 2, 3]
    result: Dict[str, int] = create_dict(keys, values)
    print(f"Created dictionary: {result}")
