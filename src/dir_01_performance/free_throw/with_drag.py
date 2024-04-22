import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 0.4  # Mass in kilograms
h = 0.75  # Initial height in meters
g = 9.81  # Acceleration due to gravity in m/s²
rho = 1.225  # Air density in kg/m³
Cd = 0.05  # Drag coefficient for a glider (usually lower than that for a sphere)
A = 0.1  # Cross-sectional area in m² (assumed based on glider dimensions)
dt = 0.001  # Time step in seconds

# Initial conditions
v0 = 6  # Initial velocity in m/s
launch_angle = 30  # Launch angle in degrees, horizontal for simplicity
vx = v0 * np.cos(np.radians(launch_angle))  # Initial horizontal velocity
vy = v0 * np.sin(np.radians(launch_angle))  # Initial vertical velocity
x, y = 0, h

# Lists to store trajectory points
x_points = [x]
y_points = [y]

# Simulation loop
while y > 0:
    v = np.sqrt(vx**2 + vy**2)  # Magnitude of velocity
    Fd = 0.5 * rho * Cd * A * v**2  # Drag force
    Fdx = Fd * (vx/v)  # Drag force in x-direction
    Fdy = Fd * (vy/v)  # Drag force in y-direction

    # Update velocities
    vx -= (Fdx/m) * dt
    vy -= (g + (Fdy/m)) * dt

    # Update positions
    x += vx * dt
    y += vy * dt

    # Store positions
    x_points.append(x)
    y_points.append(y)

# Plotting the trajectory
plt.figure(figsize=(8, 4))
plt.plot(x_points, y_points)
plt.title('Glider Motion with Drag and Weight')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()
