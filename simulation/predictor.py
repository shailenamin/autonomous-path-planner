def predict_positions(current_pos, velocity=(0, 0.1), steps=10):
    x, y = current_pos[0]
    vx, vy = velocity
    return [(x + i * vx, y + i * vy) for i in range(1, steps + 1)]
