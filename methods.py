# Method
# - it is a function that's inside a class.

class Car:
    def __init__ (self, brand: str, horsepower: int) -> None:       #first def attributes
        self.brand = brand          #assigning values to the instance of the car
        self.horsepower = horsepower

    def drive(self) -> None:                #second and third def methods
        print(f'{self.brand} is driving!')     #self refers to the instance of the class

    def get_info(self, var: int) -> None:
        print(var)
        print(f'{self.brand} with {self.horsepower} horsepower')

volvo: Car = Car('Volvo', 200)
volvo.drive()
volvo.get_info(10)

bmw: Car = Car ('BMW', 240)
bmw.drive()