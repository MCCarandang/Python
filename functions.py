#Creating resusable codes using function

from datetime import datetime

def show_date() -> None:
    print('This is the current date and time')
    print(datetime.now())

show_date()

#--------------------------------------------

#1 Functions with parameters

def greet(name: str) -> None:
    print(f'Hello, {name}!')

greet('Bob')
greet('Luigi')

#--------------------------------------------

#2 Functions returning results

def add(a: float, b: float) -> float:
    return a + b

print(add(1, 2))