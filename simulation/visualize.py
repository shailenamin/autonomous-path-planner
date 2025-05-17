import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

class Visualizer:
    def __init__(self, env):
        self.env = env
        self.fig, self.ax = plt.subplots()

    def render(self, vehicle, goal, path, obstacles):
        self.ax.clear()
        self.ax.set_xlim(0, self.env.width)
        self.ax.set_ylim(0, self.env.height)
        self.ax.plot(goal[0], goal[1], 'gx')
        self.ax.plot(vehicle.x, vehicle.y, 'ro')
        if path:
            px, py = zip(*path)
            self.ax.plot(px, py, 'b--')
        if obstacles:
            for ox, oy in obstacles:
                self.ax.add_patch(patches.Circle((ox, oy), 1, color='gray'))
        plt.pause(0.01)
