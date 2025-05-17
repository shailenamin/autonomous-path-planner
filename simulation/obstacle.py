import numpy as np

class Obstacle:
    def __init__(self, path_type='sine', bounds=(5, 15)):
        self.path_type = path_type
        self.bounds = bounds

    def update(self, t):
        if self.path_type == 'sine':
            return [(10, 10 + 3 * np.sin(t * 0.1))]
        return [(10, 10)]
