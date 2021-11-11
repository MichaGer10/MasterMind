from helper import Color, CodeBreaker, CodeMaker

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
        game.code_feedback.append([-1 for i in range(0, 5)])

        for idx, color in enumerate(self.cb.field[move_number]):
            if color == self.cm.secret_code[idx]:
                self.code_feedback[move_number][idx] = 1

            else:
                self.code_feedback[move_number][idx] = -1
        
        for idx, color in enumerate(self.cb.field[move_number]):
            if self.code_feedback[move_number][idx] != 1:
                if color in self.cm.secret_code:
                    if self.code_feedback[self.cm.secret_code.index(color)] != 1:
                        self.code_feedback[move_number][idx] = 0



# game = Game()
# game.cm.create_code()

# print("Secret Code:")
# for color in game.cm.secret_code:
#     print(Color(color).name , end=" ")

# print("")
# game.cb.color_choice()

# print("\n\nColor Chooice:")
# for color in game.cb.field[0]:
#     print(Color(color).name , end=" ")

# game.get_feedback(0)

# print("\nFeedback: ")
# for feedback in game.code_feedback[0]:
#     print(feedback, end=" ")


