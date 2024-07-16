import numpy as np
from pong_env import PongEnv

env = PongEnv()

action_space = env.action_space.n
state_space = env.observation_space.shape[0]
q_table = np.zeros((state_space, action_space))

total_episodes = 1000
learning_rate = 0.1
max_steps = 100
gamma = 0.99
epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.005

for episode in range(total_episodes):
    state = env.reset()
    total_rewards = 0

    for step in range(max_steps):
        exp_exp_tradeoff = np.random.uniform(0, 1)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(q_table[state])
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)
        q_table[state][action] = q_table[state][action] + learning_rate * (reward + gamma * np.max(q_table[new_state]) - q_table[state][action])

        state = new_state
        total_rewards += reward

        if done:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

print("Training completed")

env.close()
