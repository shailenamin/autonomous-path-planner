import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Visualizer:
    def __init__(self, env):
        self.env = env
        self.fig, self.ax = plt.subplots()
        self.trail = []

    def render(self, vehicle, goal, path, obstacles, predictions=None):
        self.ax.clear()
        self.ax.set_xlim(0, self.env.width)
        self.ax.set_ylim(0, self.env.height)

        # Draw goal
        self.ax.plot(goal[0], goal[1], 'gx', markersize=10, label='Goal')

        # Draw vehicle
        self.trail.append((vehicle.x, vehicle.y))
        if len(self.trail) > 100:
            self.trail.pop(0)
        trail_x, trail_y = zip(*self.trail)
        self.ax.plot(trail_x, trail_y, 'r--', alpha=0.6)
        self.ax.plot(vehicle.x, vehicle.y, 'ro', label='Vehicle')

        # Orientation
        dx = np.cos(vehicle.theta)
        dy = np.sin(vehicle.theta)
        self.ax.arrow(vehicle.x, vehicle.y, dx, dy, head_width=0.5, color='r')

        # Draw path
        if path:
            px, py = zip(*path)
            self.ax.plot(px, py, 'b--', label='Path')

        # Draw obstacles
        if obstacles:
            for ox, oy in obstacles:
                self.ax.add_patch(patches.Circle((ox, oy), 1, color='gray', alpha=0.7))

        # Draw predicted positions
        if predictions:
            for px, py in predictions:
                self.ax.add_patch(patches.Circle((px, py), 1, color='orange', alpha=0.3, linestyle='dashed'))

        self.ax.legend()
        plt.pause(0.01)
