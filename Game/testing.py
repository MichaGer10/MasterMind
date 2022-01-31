from game_class import Game
from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
import gym
from helper import Color


game = Game()

game.cm.create_code()
# print("Secret Code:")
# for color in game.cm.secret_code:
#     print(Color(color).name , end=" ")
# print("")

won = False
loose = False

while not won and not loose:

    game.cb.color_choice()

    print("\n\nColor Chooice:")
    for color in game.cb.field[game.move_counter]:
        print(Color(color).name , end=" ")

    game.get_feedback(game.move_counter)

    print("\nFeedback: ")
    print(game.code_feedback[game.move_counter])

    if game.isWon():
        print("YOU WON THE GAME!!!")
        won = True

    if game.isLoose():
        print("You Loose! Try Again!")
        loose = True
    
    game.move_counter += 1

print(game.cm.secret_code)
