from simulation.environment import Environment
from simulation.vehicle import Vehicle
from simulation.planner import AStarPlanner
from simulation.controller import PIDController
from simulation.obstacle import Obstacle
from simulation.visualize import Visualizer
import numpy as np

# Initialize
env = Environment(width=20, height=20)
vehicle = Vehicle(x=2, y=2, theta=0)
goal = (17, 17)
planner = AStarPlanner(env)
controller = PIDController()
obstacle = Obstacle(path_type='sine', bounds=(5, 15))
visualizer = Visualizer(env)

# Simulate
for step in range(100):
    obs_pos = obstacle.update(step)
    path = planner.plan(start=(vehicle.x, vehicle.y), goal=goal, obstacle_positions=[obs_pos])
    if path:
        next_point = path[min(1, len(path)-1)]
        steering, speed = controller.control(vehicle, next_point)
        vehicle.move(steering, speed)
    env.update_obstacle(obs_pos)
    visualizer.render(vehicle, goal, path, obs_pos)
