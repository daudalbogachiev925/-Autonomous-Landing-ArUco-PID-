from src.pid import PID

def test_pid_output_limits():
    p = PID(1, 0, 0, -0.5, 0.5)
    assert p.step(100, 0.1) == 0.5

def test_pid_integral():
    p = PID(0, 1, 0)
    p.step(1, 0.5)
    assert abs(p.step(1, 0.5) - 1.0) < 1e-6
