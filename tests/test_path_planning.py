from simulation.environment import Environment
from simulation.planner import AStarPlanner

def test_astar_basic():
    env = Environment(10, 10)
    planner = AStarPlanner(env)
    path = planner.plan((0, 0), (5, 5))
    assert path[0] == (0, 0)
    assert path[-1] == (5, 5)
