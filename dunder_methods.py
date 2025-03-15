# Dunder Methods (MAGIC METHODS) double underscore method
# - it defines the behavior of objects for built-in operations like additions, string representation,
#   comparison, iteration, etc.

class Car:
    def __init__ (self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self) -> str:                       #string dunder method
        return f'{self.brand}, {self.horsepower}'
    
    def __add__(self, other) ->str:               #add cars together
        return f'{self.brand} & {other.brand}'

volvo: Car = Car('Volvo', 200)
bmw : Car = Car('BMW', 240)

print(volvo + bmw)