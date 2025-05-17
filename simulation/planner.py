import heapq
import numpy as np

class AStarPlanner:
    def __init__(self, env):
        self.env = env

    def heuristic(self, a, b):
        return np.hypot(b[0] - a[0], b[1] - a[1])

    def plan(self, start, goal, obstacle_positions=[]):
        start = (int(start[0]), int(start[1]))
        goal = (int(goal[0]), int(goal[1]))
        queue = [(0, start)]
        came_from = {}
        cost = {start: 0}

        while queue:
            _, current = heapq.heappop(queue)
            if current == goal:
                break
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if not (0 <= neighbor[0] < self.env.width and 0 <= neighbor[1] < self.env.height):
                    continue
                if self.env.is_occupied(*neighbor) or neighbor in obstacle_positions:
                    continue
                new_cost = cost[current] + 1
                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    priority = new_cost + self.heuristic(goal, neighbor)
                    heapq.heappush(queue, (priority, neighbor))
                    came_from[neighbor] = current

        path = []
        node = goal
        while node != start:
            path.append(node)
            node = came_from.get(node, start)
        path.append(start)
        path.reverse()
        return path
