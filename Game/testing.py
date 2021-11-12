import game_class
from helper import Color

game = game_class.Game()
game.cm.create_code()

print("Secret Code:")
for color in game.cm.secret_code:
    print(Color(color).name , end=" ")

print("")

game.cb.color_choice()

print("\n\nColor Chooice:")
for color in game.cb.field[0]:
    print(Color(color).name , end=" ")

game.get_feedback(0)

print("\nFeedback: ")
for feedback in game.code_feedback[0]:
    print(feedback, end=" ")