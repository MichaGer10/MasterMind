from gym import Env
from gym.spaces import Box
from game_class import Game
import numpy as np

class CodeBreaker_Machine_Env(Env):
    def __init__(self):
        self.mastermind = Game()

        self.action_space = Box(low=0, high=7, shape=(5,), dtype=np.uint8)
        self.observation_space = Box(low=0, high=2, shape=(5,), dtype=np.uint8)

        self.move_counter = 0

    def step(self, action):
        
        action = np.round(action * 4)
        action = np.clip(action, 0, 7)
        


        done = False

        #apply action
        self.mastermind.set_next_move(action)
        move_feedback = np.array(self.mastermind.get_feedback(self.move_counter), dtype=np.uint8)

        #Calculate reward
        if self.mastermind.isWon():
            reward = 1000
            done = True
        elif np.mean(move_feedback) > np.mean(self.mastermind.get_feedback_move(self.move_counter - 1)):
            reward = -1
        else:
            reward = -5

        if self.mastermind.isLoose():
            reward = -1000
            done = True

        info = {}
        
        #increment intern counter
        self.move_counter += 1

        return move_feedback, reward, done, info
             
        

    def render(self):
        #TODO Implement Visualization
        pass

    def reset(self):

        ret_val = np.array(self.mastermind.get_feedback_move(self.move_counter), dtype=np.uint8)

        self.mastermind.initialize_game()
        self.move_counter = 0

        return ret_val
