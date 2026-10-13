import cv2
import numpy as np

class PoseEstimator:
    def __init__(self, K, dist, marker_size=0.3):
        self.K = K
        self.dist = dist
        self.marker_size = marker_size

    def estimate(self, corners):
        half = self.marker_size / 2
        obj_pts = np.array([
            [-half,  half, 0],
            [ half,  half, 0],
            [ half, -half, 0],
            [-half, -half, 0],
        ], dtype=np.float32)
        img_pts = corners.reshape(4, 2).astype(np.float32)
        ok, rvec, tvec = cv2.solvePnP(obj_pts, img_pts, self.K, self.dist)
        if not ok:
            return None
        return {"rvec": rvec, "tvec": tvec,
                "distance": float(np.linalg.norm(tvec))}
