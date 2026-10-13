from pymavlink import mavutil
from pymavlink import mavutil as m

class MavlinkBridge:
    def __init__(self, device="udp:127.0.0.1:14550"):
        self.master = mavutil.mavlink_connection(device)
        self.master.wait_heartbeat()

    def send_velocity(self, vx, vy, vz):
        self.master.mav.set_position_target_local_ned_send(
            0, self.master.target_system, self.master.target_component,
            m.mavutil.mavlink.MAV_FRAME_BODY_NED, 0b0000111111000111,
            0, 0, 0, vx, vy, vz, 0, 0, 0, 0, 0)

    def land(self):
        self.master.mav.command_long_send(
            self.master.target_system, self.master.target_component,
            m.mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)
