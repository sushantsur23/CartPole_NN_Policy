import gym
import numpy as np
import time
from tqdm import tqdm

env = gym.make('CartPole-v0')

# def basic_policy(angle):
#     if angle<0: #falling left
#         return 0 #move left
#     else:
#         return 1  #move right

def basic_policy(pole_angle):
    if pole_angle<0: #falling left
        return 0 #move left
    return 1  #move right

total_rewards = list()

N_episodes = 200
N_Steps = 200

for episode in range(N_episodes):
    rewards = 0
    #cat position, cart velocity, pole angle, pole velocity
    observation = env.reset()
    pole_angle = observation[2]
    for step in tqdm(range(N_Steps)):
        env.render()
        action = basic_policy(pole_angle)
        observation, reward, done, info = env.step(action)
        time.sleep(0.001)
        rewards+= rewards
        if done:   #fallen
            break
    total_rewards.append(rewards)
stats = {
    "mean":np.mean(total_rewards),
    "std_dev":np.std(total_rewards),
    "min": np.min(total_rewards),
    "max":np.max(total_rewards)
}
print(stats)