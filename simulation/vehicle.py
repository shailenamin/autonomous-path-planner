import numpy as np

class Vehicle:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.v = 0.5
        self.L = 2.0

    def move(self, steering_angle, speed):
        dt = 0.1
        self.x += speed * np.cos(self.theta) * dt
        self.y += speed * np.sin(self.theta) * dt
        self.theta += (speed / self.L) * np.tan(steering_angle) * dt
