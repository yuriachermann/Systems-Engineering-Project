import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d


# Constants
g = 9.81  # Acceleration due to gravity in m/s²
rho = 1.225  # Air density in kg/m³

# # Loading data
# data = pd.read_csv('aero_coefficients.csv')  # Assume this file has 'alpha', 'Cl', 'Cd' columns
#
# # Interpolating functions
# alpha_range = data['alpha']
# cl_interp = interp1d(alpha_range, data['Cl'], kind='cubic')
# cd_interp = interp1d(alpha_range, data['Cd'], kind='cubic')


# Dynamically return coefficients
def calculate_lift_coefficient(alpha_deg):
    return alpha_deg * 0.05 + 0.3
    # return cl_interp(alpha_deg)


def calculate_drag_coefficient(alpha_deg):
    return alpha_deg * 0.01 + 0.1
    # return cd_interp(alpha_deg)


def calculate_cross_sectional_area(alpha_deg):
    return 0.001 * alpha_deg  # TODO: Implement a more realistic relationship


def calculate_motion(mass,
                     initial_height,
                     initial_velocity,
                     launch_angle,
                     min_alpha_deg,
                     dt=0.001):
    # Initial conditions
    vx = initial_velocity * np.cos(np.radians(launch_angle))
    vy = initial_velocity * np.sin(np.radians(launch_angle))
    x, y = 0, initial_height

    # Lists to store trajectory points
    x_points, y_points = [x], [y]

    # Simulation loop
    while y > 0:
        v = np.sqrt(vx ** 2 + vy ** 2)
        alpha_deg = max(np.degrees(np.arctan2(vy, vx)), min_alpha_deg)  # Enforcing minimum angle of attack

        # Dynamic lift and drag coefficients
        lift_coefficient = calculate_lift_coefficient(alpha_deg)
        drag_coefficient = calculate_drag_coefficient(alpha_deg)

        # Calculate forces
        drag_force = 0.5 * rho * drag_coefficient * calculate_cross_sectional_area(alpha_deg) * v ** 2
        lift_force = 0.5 * rho * lift_coefficient * calculate_cross_sectional_area(alpha_deg) * v ** 2
        drag_force_x = drag_force * (vx / v)
        drag_force_y = drag_force * (vy / v)
        lift_force_y = lift_force * (vx / v)  # Lift force in y-direction

        # Update velocities
        vx -= (drag_force_x / mass) * dt
        vy += (lift_force_y / mass) * dt - (g + (drag_force_y / mass)) * dt

        # Update positions
        x += vx * dt
        y += vy * dt

        # Store positions
        x_points.append(x)
        y_points.append(y)

    return x_points, y_points


if __name__ == '__main__':
    x_list, y_list = calculate_motion(
        mass=0.4,  # Mass [kg]
        initial_height=1,  # Initial height [m]
        initial_velocity=7,  # Initial velocity [m/s]
        launch_angle=40,  # Launch angle [degrees]
        min_alpha_deg=1,  # Minimum angle of attack in degrees
        dt=0.001,  # Time step [s]
    )

    plt.figure(figsize=(8, 4))
    plt.plot(x_list, y_list)
    plt.title('Glider Motion Simulation')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()
