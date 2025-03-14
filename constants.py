#Constants are variables whose values should not change once assigned
#It is defined using uppercase letters with underscores_for separating words

PI = 3.14159
GRAVITY = 9.81
APP_NAME = "Timekeeping System"

#IMPORT AND USE THE CONSTANTS

# import constants

# print(constants.PI)
# print(constants.GRAVITY)

#USING dataclasses FOR CONSTANTS

from dataclasses import dataclass

@dataclass(frozen=True) #makes the class immutable, preventing accidental modifications
class Config:
    DATABASE_NAME: str = "timekeeping.db"
    RFID_READER_PORT: str = "/dev/ttyUSB0"

print(Config.DATABASE_NAME)


#Another example

from typing import Final

VERSION : Final[str] = '1.0.12'
PI: Final[float] = 3.1415