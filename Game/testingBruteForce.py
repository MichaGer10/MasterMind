from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
from game_class import Game
import gym
import random

env = gym.make("mastermind-v0")

for episode in range(0, 10000000):
    state = env.reset()
    done = False
    reward_total = 0
    
    while not done:
        action = [random.randint(0, 7) for i in range(0, 5)]
        n_state, reward, done, info = env.step(action)
        reward_total += reward

    if reward_total > -1000 :
        print("Episode: " + str(episode) + " Reward: " + str(reward_total))
    print(state)
    break
