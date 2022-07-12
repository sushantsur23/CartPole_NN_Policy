from bdb import Breakpoint
import gym
import numpy as np
import time
from tqdm import tqdm

env = gym.make("CartPole-v1")

# def basic_policy(PoleAngle):
#     if PoleAngle < 0: # falling left
#         return 0 # Move left
#     else: # Move right
#         return 1 
def basic_policy(PoleAngle):
    if PoleAngle < 0: # falling left
        return 0 # Move left
    return 1 

total_rewards = list()

N_episodes = 200
N_steps = 200

for episode in range(N_episodes):
    rewards = 0
    # CartPoistion, CartVelocity, PoleAngle, PoleAngularVelocity
    Observations = env.reset()
    PoleAngle = Observations[2]
    for step in tqdm(range(N_steps)):
        env.render()
        action = basic_policy(PoleAngle)
        Observations, reward, done, info = env.step(action)
        time.sleep(0.001) # sleep
        rewards += reward
        if done: # Fallen
            break
    total_rewards.append(rewards)

stats = {
    "mean": np.mean(total_rewards),
    "std": np.std(total_rewards),
    "min": np.min(total_rewards),
    "max": np.max(total_rewards)
}

print(stats)