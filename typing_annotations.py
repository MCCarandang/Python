#Type annotations indicate the expected data types of variables, functions, parameters, and return values


#Variable Type Annotations
# - you can specify the expected type of a variable using 

name: str = 'Alice'
age: int = 30
height: float = 5.9
is_active: bool = True

print(f'{name} is already {age} with a height of {height}'.format(name, age, height))

#Function Type Annotations
# - you can annotate parameters and return values

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

#Multiple Parameter Types
# - use Union from the typing module

from typing import Union

def square(number: Union[int, float]) -> float:
    return number * number