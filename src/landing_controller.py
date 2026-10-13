from src.pid import PID

class LandingController:
    def __init__(self, target_dist=0.5):
        self.target_dist = target_dist
        self.pid_x = PID(0.8, 0.05, 0.1)
        self.pid_y = PID(0.8, 0.05, 0.1)
        self.pid_z = PID(1.0, 0.1, 0.15)

    def compute(self, pose, dt):
        tx, ty, tz = pose["tvec"].flatten()
        ex, ey = tx, ty
        ez = tz - self.target_dist
        return {
            "vx": self.pid_x.step(ex, dt),
            "vy": self.pid_y.step(ey, dt),
            "vz": self.pid_z.step(ez, dt),
        }
