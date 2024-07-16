import gym
from gym import spaces
import numpy as np
import pygame

class PongEnv(gym.Env):
    def __init__(self):
        super(PongEnv, self).__init__()
        self.screen_width = 800
        self.screen_height = 600
        self.bar_width = 10
        self.bar_height = 100
        self.ball_size = 20
        self.bar_speed = 5
        self.ball_speed = 5

        self.action_space = spaces.Discrete(3)  # 0: Up, 1: Down, 2: Stay
        self.observation_space = spaces.Box(
            low=np.array([0, 0, 0, 0]),
            high=np.array([self.screen_height, self.screen_width, self.screen_height, self.screen_width]),
            dtype=np.float32
        )

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong AI')

    def reset(self):
        self.bar_y = self.screen_height // 2 - self.bar_height // 2
        self.ball_x = self.screen_width // 2 - self.ball_size // 2
        self.ball_y = self.screen_height // 2 - self.ball_size // 2
        self.ball_speed_x = self.ball_speed
        self.ball_speed_y = self.ball_speed
        return np.array([self.bar_y, self.ball_x, self.ball_y, self.ball_speed_x])

    def step(self, action):
        if action == 0 and self.bar_y > 0:
            self.bar_y -= self.bar_speed
        elif action == 1 and self.bar_y < self.screen_height - self.bar_height:
            self.bar_y += self.bar_speed

        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        if self.ball_y <= 0 or self.ball_y >= self.screen_height - self.ball_size:
            self.ball_speed_y *= -1
        if self.ball_x <= 0:
            self.ball_x, self.ball_y = self.screen_width // 2 - self.ball_size // 2, self.screen_height // 2 - self.ball_size // 2
            self.ball_speed_x, self.ball_speed_y = self.ball_speed, self.ball_speed
        if self.ball_x >= self.screen_width - self.ball_size:
            self.ball_speed_x *= -1

        if self.bar_x < self.ball_x < self.bar_x + self.bar_width and self.bar_y < self.ball_y < self.bar_y + self.bar_height:
            self.ball_speed_x *= -1

        reward = 1 if self.bar_x < self.ball_x < self.bar_x + self.bar_width and self.bar_y < self.ball_y < self.bar_y + self.bar_height else -1
        done = self.ball_x < 0 or self.ball_x > self.screen_width

        obs = np.array([self.bar_y, self.ball_x, self.ball_y, self.ball_speed_x])
        return obs, reward, done, {}

    def render(self, mode='human'):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.bar_x, self.bar_y, self.bar_width, self.bar_height))
        pygame.draw.ellipse(self.screen, (255, 255, 255), (self.ball_x, self.ball_y, self.ball_size, self.ball_size))
        pygame.display.flip()

    def close(self):
        pygame.quit()

env = PongEnv()
obs = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()
