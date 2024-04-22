import numpy as np


class Glider:
    def __init__(self, glider_mass, payload_mass, wing_area, wing_span):
        self.glider_mass = glider_mass
        self.payload_mass = payload_mass
        self.wing_area = wing_area
        self.wing_span = wing_span


class Launch:
    def __init__(self, initial_height, initial_velocity, launch_angle):
        self.initial_height = initial_height
        self.initial_velocity = initial_velocity
        self.launch_angle = launch_angle

    @property
    def initial_velocity_x(self):
        return self.initial_velocity * np.cos(np.radians(self.launch_angle))

    @property
    def initial_velocity_y(self):
        return self.initial_velocity * np.sin(np.radians(self.launch_angle))

    @property
    def alpha_deg(self):
        return max(np.degrees(np.arctan2(self.initial_velocity_y, self.initial_velocity_x)), 5)

    @property
    def time_of_flight(self):
        return (self.initial_velocity_y + np.sqrt(self.initial_velocity_y**2 + 2 * 9.81 * self.initial_height)) / 9.81

    @property
    def time_intervals(self):
        return np.linspace(0, self.time_of_flight, num=100)

    @property
    def launch_data(self):
        return self.initial_height, self.initial_velocity, self.launch_angle


aero_glider = Glider(0.4, 0.1, 0.1, 0.5)
aero_launch = Launch(1, 7, 40)

print(aero_glider.glider_mass, aero_glider.payload_mass, aero_glider.wing_area, aero_glider.wing_span)
print(aero_launch.initial_height, aero_launch.initial_velocity, aero_launch.launch_angle)