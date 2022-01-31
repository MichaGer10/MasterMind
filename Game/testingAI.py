from os import terminal_size
from tensorflow.python.keras.layers.core import Reshape
from mastermind.mastermind_env.envs.mastermind_env import CodeBreaker_Machine_Env
from game_class import Game
import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, UpSampling1D, Conv1D
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy, Policy
from rl.memory import SequentialMemory


env = gym.make("mastermind-v0")


model = Sequential()
model.add(Conv1D(1, kernel_size=(5), padding="same", activation="relu", input_shape=(5,1)))
model.add(Conv1D(2, kernel_size=(5), padding="same", activation="relu"))
model.add(Conv1D(4, kernel_size=(5), padding="same", activation="relu"))
model.add(Conv1D(7, kernel_size=(5), padding="same", activation="relu"))
model.add(Flatten())
#Bisheriges Netz
#model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(5, activation='sigmoid'))
model.add(Reshape((5,1)))

model.summary()

policy = BoltzmannQPolicy()
memory = SequentialMemory(limit=50000, window_length=1)
dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=[5, 1], nb_steps_warmup=10, target_model_update=1e-2)

dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])
dqn.fit(env=env, nb_steps=50000, visualize=False, verbose=1)