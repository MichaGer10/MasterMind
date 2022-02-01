from helper import CodeBreaker, CodeMaker
from random import shuffle

class Game():

    def __init__(self) -> None:
        self.cm = CodeMaker()
        self.cb = CodeBreaker()
        self.code_feedback = []
        self.code_feedback.append([0 for i in range(0, 5)])
        self.GAMELENGTH = 10
        self.move_counter = 0

    def initialize_game(self):
        self.cm.create_code()
        self.cb.field.clear()
        self.cb.field = []
        self.code_feedback.clear()
        self.code_feedback.append([0 for i in range(0, 5)])
        self.move_counter = 0

    def set_next_move(self, action):
        self.cb.field.append(action)
        self.move_counter += 1

    def get_feedback_move(self, move):
        return self.code_feedback[move]


    def get_feedback(self, move_number):
        #initialize helper list
        wrong_colors = []

        #Find correct guessed colors and guessed places in secret code
        for idx, color in enumerate(self.cb.field[move_number]):
            if color == self.cm.secret_code[idx]:
                self.code_feedback[move_number][idx] = 2

            else:
                self.code_feedback[move_number][idx] = 0
                wrong_colors.append(self.cm.secret_code[idx])

        #Find correct guessed colors in secret code
        for idx, color in enumerate(self.cb.field[move_number]):
            if self.code_feedback[move_number][idx] != 2:
                if color in wrong_colors:
                    self.code_feedback[move_number][idx] = 1
                    wrong_colors.remove(color)
        
        #multiple shuffle feedback list
        for i in range(0,5):
            shuffle(self.code_feedback[move_number])

        self.code_feedback.append([0 for i in range(0, 5)])

        return self.code_feedback[move_number]

    def isWon(self):
        if self.code_feedback[self.move_counter - 1] == [2, 2, 2, 2, 2]:
            return True
        else:
            return False

    def isLoose(self):
        if len(self.cb.field) >= self.GAMELENGTH:
            return True
        else:
            return False