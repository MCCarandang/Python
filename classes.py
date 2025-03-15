# Class is a blueprint for creating objects. 
# - it defines attributes (variables) and methods (functions) that operate on the object.


#Initializer __int__ is use to set up and instance of the class

class Car:
    def __init__ (self, colour: str, horsepower: int) -> None:
        self.colour = colour                #assigning values to the instance of the car
        self.horsepower = horsepower        #assigning values to the instance of the car

volvo: Car = Car('red', 200)           #volvo is the instance of the class or an object of the class
print(volvo.colour)
print(volvo.horsepower)

bmw: Car = Car('yellow', 240)
print(bmw.colour)
print(bmw.horsepower)

#Classes simplify the process of creating objects or code that has to be duplicated a lot.