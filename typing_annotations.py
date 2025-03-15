#Type annotations indicate the expected data types of variables, functions, parameters, and return values


#1 Variable Type Annotations
# - you can specify the expected type of a variable using 

name: str = 'Alice'
age: int = 30
height: float = 5.9
is_active: bool = True

print(f'{name} is already {age} with a height of {height}'.format(name, age, height))

#-------------------------------------------------

#2 Function Type Annotations
# - you can annotate parameters and return values

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

#-------------------------------------------------

#3 Multiple Parameter Types
# - use Union from the typing module

from typing import Union    #Union ensures that the fuction can handle both integers and floats

def square(number: Union[int, float]) -> float:
    return number * number

print(square(4))
print(square(3.5))

#-------------------------------------------------

#4 Annotating Lists, Tuples, and Dictionaries

from typing import List, Tuple, Dict

numbers: List[int] = [1, 2, 3, 4]
coordinates: Tuple[float, float] = (40.7128, -74.0060)
employee_data: Dict[str, int] = {"Alice":30, "Bob": 25}

print("Numbers List:", numbers)
print("First number:", numbers[0])
print("First number:", numbers[1])

print("\nCoordinates (Latitude, Longitude):", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

print("\nEmployee Data:", employee_data)
print("Alice's Age:", employee_data["Alice"])
print("Bob's Age:", employee_data["Bob"])

# Iterating through dictionary
print("\nEmployee Names and Ages:")



#-------------------------------------------------

#5 Optional Types
# - when a value can be none :

from typing import Optional

def get_user(name: str) -> Optional[dict]:
    users = {"Alice": {"age": 30}, "Bob": {"age": 25}}
    return users.get(name)

print(get_user('Alice'))
print(get_user('Bob'))

#-------------------------------------------------

#6 Type Aliases
# - ensures consistency and improves code readability

from typing import Dict

User = Dict[str, str]       # Alias for a dictionary with string keys and values

user1: User = {"name": "Alice", "role": "Admin"}

# Print the whole dictionary
print("User Data:", user1)

# Print each value separately
print("Name:", user1["name"])
print("Role:", user1["role"])

# Formatted string output
print(f"User {user1['name']} has the role of {user1['role']}.")

#-------------------------------------------------

#7 Using Typeddict for Structures Dictionaries
# - for more strict typing of dictionaries

from typing import TypedDict

class Employee(TypedDict):
    name: str
    age: int
    department: str

employee: Employee = {"name": "Alice", "age": 30, "department": "HR"}

# Print the whole dictionary
print("Employee Data:", employee)

# Print each value separately
print("Name:", employee["name"])
print("Age:", employee["age"])
print("Department:", employee["department"])

# Formatted string output
print(f"Employee {employee['name']} is {employee['age']} years old and works in {employee['department']} department.")

#-------------------------------------------------

#8 Type Annotations for Classes

class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def get_info(self) -> str:
        return f'{self.name} is {self.age} yearls old.'
    
p = Person("Alice", 30)
print(p.get_info())

#-------------------------------------------------

#9 Any Type for Dynamic Typing
# - use Any when a variable can be any type

from typing import Any

def display_value(data: Any) -> None:
    print(f'Value: {data}, Type: {type(data)}')

#Testing with different types
display_value("Hello")
display_value(100)
display_value(True)
display_value([1, 2, 3])

#-------------------------------------------------

#10 Callable Types (Functions as Arguments)
# - when a function takes another function as a parameter
# - allows functions to accept other functions as arguments
# - ensures type safety

from typing import Callable

def process_data(data: str, callback: Callable[[str], str]) -> str:
    return callback(data)

def uppercase(text: str) -> str:
    return text.upper()

print(process_data("hello", uppercase))

#-------------------------------------------------

#11 Generic Types
# - for reusable type-safe functions and classes

from typing import TypeVar, Generic

T = TypeVar("T") # Generic Type that allows a class to accept a type parameter

class Box(Generic[T]):      #T is a type variable (It represents a placeholder for any type (int, str, float, etc.)
    def __init__(self, content: T):
        self.content = content

int_box = Box(10)
str_box = Box("Hello")
bool_box = Box(True)

print(int_box.content)
print(str_box.content)
print(bool_box.content)
