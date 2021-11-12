from helper import Color, CodeBreaker, CodeMaker
from random import shuffle

class Game():

    def __init__(self) -> None:
        self.cm = CodeMaker()
        self.cb = CodeBreaker()
        self.code_feedback = []

    def initialize_game(self):
        self.cm.create_code()
        self.cb.field.clear
        self.cb.field = []
        self.code_feedback = []


    def get_feedback(self, move_number):

        #initialize feedback list and helper list
        self.code_feedback.append([-1 for i in range(0, 5)])
        wrong_colors = []

        #Find correct guessed colors and guessed places in secret code
        for idx, color in enumerate(self.cb.field[move_number]):
            if color == self.cm.secret_code[idx]:
                self.code_feedback[move_number][idx] = 1

            else:
                self.code_feedback[move_number][idx] = -1
                wrong_colors.append(self.cm.secret_code[idx])

        #Find correct guessed colors in secret code
        for idx, color in enumerate(self.cb.field[move_number]):
            if self.code_feedback[move_number][idx] != 1:
                if color in wrong_colors:
                    self.code_feedback[move_number][idx] = 0
                    wrong_colors.remove(color)
        
        #multiple shuffle feedback list
        for i in range(0,5):
            shuffle(self.code_feedback[move_number])
