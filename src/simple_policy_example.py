import gym
import numpy as np
import time

env = gym.make('CartPole-v0')

Observations = env.reset()
print(Observations)

for _ in range(100):
    env.render()