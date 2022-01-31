import random
from enum import Enum

class CodeMaker():

    def create_code(self):
        self.secret_code = (random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7))


class CodeBreaker():
    
    def __init__(self) -> None:
        self.field = []

    #TODO adjust function for GUI
    def color_choice(self):
        colors = []
        for i in range(1, 6):
            color = input("Color " + str(i) + ": ")
            colors.append(int(color))

        self.field.append(colors)

            

class Color(Enum):
    RED = 0
    BLUE = 1
    NEON_GREEN = 2
    YELLOW = 3
    PURPLE = 4
    TURQUOISE = 5
    ORANGE = 6
    DEEP_GREEN = 7
