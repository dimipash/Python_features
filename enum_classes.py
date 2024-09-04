"""
This code demonstrates the use of enum classes in Python.
Enums are a feature in Python that provide a convenient way to create a set of named constants.
In this example, the Color, Direction, Status, Priority, Permissions, and FileMode classes are enums that have a name and value.
The Direction and Status enums are also unique, which means that no two members can have the same value.
The Priority enum is an IntEnum, which allows comparison with integers.
The Permissions and FileMode enums are Flag enums, which allow bitwise operations.
"""

from enum import Enum, auto, unique, IntEnum, Flag, IntFlag


# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Enum with auto()
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


# Unique Enum
@unique
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    # DUPLICATE = 1  # This would raise a ValueError due to @unique


# IntEnum
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


# Flag Enum
class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


# IntFlag Enum
class FileMode(IntFlag):
    READ = 4
    WRITE = 2
    EXECUTE = 1


if __name__ == "__main__":
    # Basic Enum usage
    print(f"Color.RED: {Color.RED}, value: {Color.RED.value}")
    print(f"Color(2): {Color(2)}")

    # Iterating over Enum members
    print("\nAll Direction members:")
    for direction in Direction:
        print(f"{direction.name}: {direction.value}")

    # Enum comparison
    print(f"\nColor.RED == Color.RED: {Color.RED == Color.RED}")
    print(f"Color.RED == Color.BLUE: {Color.RED == Color.BLUE}")

    # IntEnum allows comparison with integers
    print(f"\nPriority.LOW < Priority.HIGH: {Priority.LOW < Priority.HIGH}")
    print(f"Priority.MEDIUM == 2: {Priority.MEDIUM == 2}")

    # Flag Enum operations
    user_permissions = Permissions.READ | Permissions.WRITE
    print(f"\nUser permissions: {user_permissions}")
    print(f"Has read permission: {Permissions.READ in user_permissions}")
    print(f"Has execute permission: {Permissions.EXECUTE in user_permissions}")

    # IntFlag Enum operations
    file_mode = FileMode.READ | FileMode.WRITE
    print(f"\nFile mode: {file_mode}")
    print(f"File mode value: {file_mode.value}")
    print(f"Can read: {FileMode.READ in file_mode}")
    print(f"Can execute: {FileMode.EXECUTE in file_mode}")
