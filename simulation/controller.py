import numpy as np

class PIDController:
    def __init__(self):
        self.kp = 1.0

    def control(self, vehicle, target_point):
        dx = target_point[0] - vehicle.x
        dy = target_point[1] - vehicle.y
        desired_theta = np.arctan2(dy, dx)
        error = desired_theta - vehicle.theta
        steering = self.kp * error
        return steering, vehicle.v
