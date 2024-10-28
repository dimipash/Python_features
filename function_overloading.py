from functools import singledispatch


@singledispatch
def process_data(data):
    """Base function for processing different types of data."""
    raise NotImplementedError("Unsupported type")


@process_data.register(str)
def _(data: str):
    """Handles string data by converting to uppercase."""
    return f"Processing string: {data.upper()}"


@process_data.register(int)
def _(data: int):
    """Handles integer data by multiplying by 2."""
    return f"Processing integer: {data * 2}"


@process_data.register(list)
def _(data: list):
    """Handles list data by computing the sum."""
    return f"Processing list: {sum(data)}"


# Usage
print(process_data("hello"))
print(process_data(42))
print(process_data([1, 2, 3]))
