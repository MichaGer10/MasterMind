from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
from game_class import Game
import gym
from stable_baselines3.common import env_checker

env = gym.make("mastermind-v0")

env.close()

env_checker.check_env(env)