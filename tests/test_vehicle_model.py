from simulation.vehicle import Vehicle

def test_vehicle_move():
    v = Vehicle(0, 0, 0)
    v.move(0, 1)
    assert v.x > 0
