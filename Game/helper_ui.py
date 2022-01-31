from enum import Enum

<<<<<<< HEAD
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

            

=======
>>>>>>> Verknüpfen-Ui
class Color(Enum):
    RED = (255,0,0)
    BLUE = (0,0,255)
    NEON_GREEN = (0,255,0)
    YELLOW = (255,255,0)
    PURPLE = (255,0,255)
    TURQUOISE = (0,255,255)
    ORANGE = (255,128,0)
    DEEP_GREEN = (0,100,0)