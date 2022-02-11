import os
from trainAndLog import TrainAndLoggingCallback
from stable_baselines3 import PPO, TD3, SAC, A2C
from stable_baselines3.common.env_util import make_vec_env

from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
from game_class import Game
import gym



CHECKPOINT_DIR = os.path.join(os.path.dirname(os.getcwd()), './data/train_mastermind/')
LOG_DIR = os.path.join(os.path.dirname(os.getcwd()), './data/log/')

callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)

env = gym.make("mastermind-v0")

model = PPO('MlpPolicy', env, tensorboard_log=LOG_DIR, verbose=1, learning_rate=0.0000001, n_steps=16384, clip_range=.1, gamma=.99, gae_lambda=.9)

model.learn(total_timesteps=10000000)