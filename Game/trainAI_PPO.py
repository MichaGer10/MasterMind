import os
from trainAndLog import TrainAndLoggingCallback
from stable_baselines3 import PPO
from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
from game_class import Game
import gym



CHECKPOINT_DIR = os.path.join(os.path.dirname(__file__), './AI/data/train_mastermind')
LOG_DIR = os.path.join(os.path.dirname(__file__), './AI/log/')

callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)

env = gym.make("mastermind-v0")

model = PPO('MlpPolicy', env, tensorboard_log=LOG_DIR, verbose=1, learning_rate=0.0001, n_steps=256)

model.learn(total_timesteps=100000)