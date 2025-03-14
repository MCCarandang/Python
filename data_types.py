#Basic Data Types
from enum import unique


number: int = 10
decimal: float = 2.5
text: str = 'Hello'
active: bool = True

names: list = ['bob', 'anna', 'luigi'] #can add or remove elements
coordinates: tuple = (1.5, 2.5) #immutable, you cannot perform any operations here
unique: set = {1, 4, 2,9} #everythinh dhould be unique, can't have any duplicate
data: dict = {'name', 'bob', 'age', 20} #stores key-value pairs