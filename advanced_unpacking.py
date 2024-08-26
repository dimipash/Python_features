# Basic Unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extended Iterable Unpacking with *
a, *b, c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}\n")

# Ignoring Values
_, _, c = [1, 2, 3]

# Unpacking Nested Structures
data = ("Alice", (25, "Engineer"))
name, age, profession = data


# Unpacking in Function Arguments
def print_names(*names):
    for name in names:
        print(name)


print_names("Alice", "Bob", "Charlie")

# Combining Lists with Unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(*list1)
print(f"Combined List: {combined}\n")

# Unpacking Dictionaries with **
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
print(f"Combined Dictionary: {combined_dict}\n")

# Swapping Variables Using Unpacking
x = 10
y = 20
print(f"Before Swap - x: {x}, y: {y}")
x, y = y, x
print(f"After Swap - x: {x}, y: {y}\n")

# Unpacking in a for loop
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"X: {x}, Y: {y}")

print()

# Unpacking with enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()

# Unpacking in list comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"Squared numbers: {squared}")

print()

# Unpacking in dictionary comprehensions
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_lengths}")

print()


# Unpacking in function returns
def get_user_info():
    return "Alice", 30, "alice@example.com"


name, age, email = get_user_info()
print(f"User: {name}, Age: {age}, Email: {email}")

print()

# Unpacking with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print()

# Unpacking in lambda functions
point = (3, 4)
distance = lambda x, y: (x**2 + y**2) ** 0.5
print(f"Distance from origin: {distance(*point):.2f}")

print()

# Unpacking in string formatting
user = ("Alice", 30)
print("Name: {}, Age: {}".format(*user))

print()

# Unpacking with the walrus operator (Python 3.8+)
if (n := len(names)) > 2:
    print(f"There are {n} names in the list")

print()


# Unpacking in class instantiation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


coordinates = [10, 20]
point = Point(*coordinates)
print(f"Point: ({point.x}, {point.y})")
