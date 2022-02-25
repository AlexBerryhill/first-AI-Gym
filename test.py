import gym
import random
import time

env
actions = env.action_space.n

from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Dense, Flatten
from tensorflow.keras.models import Adam

def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1,states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='linear'))