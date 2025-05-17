import numpy as np

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def update_obstacle(self, positions):
        # Normalize to a list of (x, y) tuples
        if isinstance(positions, (list, tuple)) and isinstance(positions[0], (int, float)):
            self.obstacles = [tuple(positions)]
        else:
            self.obstacles = [tuple(p) for p in positions]

    def is_occupied(self, x, y):
        for pos in self.obstacles:
            ox, oy = pos
            if np.hypot(ox - x, oy - y) < 1.5:
                return True
        return False
