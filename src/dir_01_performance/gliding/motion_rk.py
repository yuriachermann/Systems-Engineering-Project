import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Acceleration due to gravity in m/s²
rho = 1.225  # Air density in kg/m³


def calculate_lift_coefficient(alpha_deg):
    return 0.3 + alpha_deg * 0.01  # Simplified relationship


def calculate_drag_coefficient(alpha_deg):
    return 0.03 + alpha_deg / 10  # Simplified relationship


def calculate_cross_sectional_area(alpha_deg):
    return 0.1  # Constant cross-sectional area for simplicity


def motion_derivatives(t, y, mass):
    vx, vy, x, y = y
    v = np.sqrt(vx**2 + vy**2)
    alpha_deg = np.degrees(np.arctan2(vy, vx))
    alpha_deg = max(alpha_deg, 5)  # Enforcing minimum angle of attack

    # Calculate dynamic coefficients
    lift_coefficient = calculate_lift_coefficient(alpha_deg)
    drag_coefficient = calculate_drag_coefficient(alpha_deg)
    A = calculate_cross_sectional_area(alpha_deg)

    # Calculate forces
    D = 0.5 * rho * drag_coefficient * A * v**2
    L = 0.5 * rho * lift_coefficient * A * v**2
    drag_force_x = D * (vx / v)
    drag_force_y = D * (vy / v)
    lift_force_y = L * (vx / v)

    # Derivatives
    dvx_dt = -drag_force_x / mass
    dvy_dt = (lift_force_y / mass) - (g + drag_force_y / mass)
    dx_dt = vx
    dy_dt = vy

    return [dvx_dt, dvy_dt, dx_dt, dy_dt]


def calculate_motion(mass, initial_height, initial_velocity, launch_angle):
    # Initial conditions
    vx = initial_velocity * np.cos(np.radians(launch_angle))
    vy = initial_velocity * np.sin(np.radians(launch_angle))
    initial_conditions = [vx, vy, 0, initial_height]

    # Time span
    t_span = (0, 10)  # Total time to simulate
    t_eval = np.linspace(0, 0.8, 100)  # Times at which to store the results

    # Solve the system
    sol = solve_ivp(motion_derivatives, t_span, initial_conditions, args=(mass,), t_eval=t_eval, method='RK45')

    return sol.t, sol.y[2], sol.y[3]


if __name__ == '__main__':
    times, x_list, y_list = calculate_motion(
        mass=0.4,  # Mass [kg]
        initial_height=1,  # Initial height [m]
        initial_velocity=7,  # Initial velocity [m/s]
        launch_angle=40  # Launch angle [degrees]
    )

    plt.figure(figsize=(8, 4))
    plt.plot(x_list, y_list)
    plt.title('Glider Motion Simulation with RK45')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

    # Print the final position
    print(f"Final position: {x_list[-1]:.2f} m")

    # Print the time of flight
    print(f"Time of flight: {times[-1]:.2f} s")

    # Print the maximum height
    print(f"Maximum height: {max(y_list):.2f} m")
