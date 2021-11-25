import random
from enum import Enum

class CodeMaker():

    def create_code(self):
        self.secret_code = (random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7))

class CodeMaker_Human(CodeMaker):

    def create_code(self):
        self.secret_code = (random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7))

class CodeMaker_Machine(CodeMaker):
    
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
            
            #is input valid?
            while not color.strip().isdigit() or int(color) > 7 or int(color) < 0:
                print("Wrong Input!!! Number must be in range 0-7")
                color = input("Color " + str(i) + ": ")

            colors.append(int(color))

        self.field.append(colors)


class CodeBreaker_Human(CodeBreaker):
    def __init__(self) -> None:
        super().__init__()

    #TODO adjust function for GUI
    def color_choice(self):
        colors = []
        for i in range(1, 6):
            color = input("Color " + str(i) + ": ")
            
            #is input valid?
            while not color.strip().isdigit() or int(color) > 7 or int(color) < 0:
                print("Wrong Input!!! Number must be in range 0-7")
                color = input("Color " + str(i) + ": ")

            colors.append(int(color))

        self.field.append(colors)


class CodeBreaker_Machine(CodeBreaker):
    def __init__(self) -> None:
        super().__init__()

    def color_choice_random(self):
        colors = [random.randint(0, 7) for i in range(0, 5)]
        self.field.append(colors)

    def get_choice(self):
        pass


            

class Color(Enum):
    RED = 0
    BLUE = 1
    NEON_GREEN = 2
    YELLOW = 3
    PURPLE = 4
    TURQUOISE = 5
    ORANGE = 6
    DEEP_GREEN = 7
